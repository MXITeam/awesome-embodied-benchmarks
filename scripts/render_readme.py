"""Render README.md and benchmarks/*.md from templates/ + data/benchmarks.yaml + data/metrics.json + data/open_source.json.

The full tables live in one page per section because GitHub truncates a README beyond 500 KiB.
Runs offline; network access is only needed by update_metrics.py.
Use `--check` in CI to fail when a generated file is out of date.
"""
from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

from common import (README, SECTION_PAGES, SECTION_TEMPLATES, TEMPLATE, code_words, data_words, found_nothing, has_code,
                    has_data, has_open, iter_entries, license_words, load_data, load_metrics, load_open, normalize_repo,
                    open_info, paper_key, plain_name)

TOP_N = 20


def resolve_repo(entry: dict, metrics: dict) -> str | None:
    slug = normalize_repo(entry.get("github")) or metrics.get("discovered_github", {}).get(paper_key(entry) or "")
    if not slug:
        return None
    info = metrics.get("repos", {}).get(slug, {})
    if info.get("missing"):
        return None
    return info.get("full_name", slug)


def paper_cell(entry: dict, metrics: dict) -> str:
    if entry.get("link"):
        return entry["link"]
    if entry.get("arxiv"):
        return f"[arXiv:{entry['arxiv']}](https://arxiv.org/abs/{entry['arxiv']})"
    if entry.get("title"):
        resolved = metrics.get("papers", {}).get(paper_key(entry), {}).get("arxiv")
        if resolved:
            return f"[arXiv:{resolved}](https://arxiv.org/abs/{resolved})"
        q = urllib.parse.quote_plus(entry["title"])
        return f"[arXiv search](https://arxiv.org/search/?query={q}&searchtype=all)"
    return "—"


def citation_cell(entry: dict, metrics: dict) -> str:
    p = metrics.get("papers", {}).get(paper_key(entry) or "")
    if not p or p.get("citations") is None:
        return "—"
    n = f"{p['citations']:,}"
    return f"[{n}]({p['url']})" if p.get("url") else n


def stars_cell(entry: dict, metrics: dict) -> str:
    slug = resolve_repo(entry, metrics)
    if not slug:
        return "—"
    # shields.io badge = live star count on every page view
    return (f"[![stars](https://img.shields.io/github/stars/{slug}?style=flat&label=%E2%AD%90&color=f5c518)]"
            f"(https://github.com/{slug})")


def to_markdown(header: list[str], rows: list[list[str]]) -> str:
    return "\n".join(["| " + " | ".join(header) + " |", "|" + "---|" * len(header)] + ["| " + " | ".join(r) + " |" for r in rows])


def render_table(table: dict, metrics: dict) -> str:
    """Platform, dataset, survey and starter tables."""
    cols = list(table["columns"])
    with_metrics = table.get("metrics", True)
    rows = []
    for e in table["entries"]:
        cells = list(e["cells"]) + [""] * (len(cols) - len(e["cells"]))
        if with_metrics:
            if e.get("no_paper") and not e.get("link") and not e.get("github"):
                cells += ["", "", ""]
            else:
                cells += [paper_cell(e, metrics), citation_cell(e, metrics), stars_cell(e, metrics)]
        rows.append(cells)
    return to_markdown(cols + (["Paper", "Citations", "GitHub ⭐"] if with_metrics else []), rows)


def render_benchmark_table(table: dict, metrics: dict, store: dict) -> str:
    """Code and Data come right after the type so they stay on screen; stars sit in the Code cell."""
    cols = list(table["columns"])
    rows = []
    for e in table["entries"]:
        cells = [c if c != "|" else "" for c in e["cells"]] + [""] * (len(cols) - len(e["cells"]))
        info = open_info(e, store)
        paper = citations = ""
        code = " · ".join(filter(None, [code_words(info), license_words(info)]))
        if not (e.get("no_paper") and not e.get("link") and not e.get("github")):
            paper, citations, stars = paper_cell(e, metrics), citation_cell(e, metrics), stars_cell(e, metrics)
            if stars != "—":
                code = stars if code in ("", "Not found") else f"{code} {stars}"
        rows.append([*cells[:3], code, data_words(info), *cells[3:], paper, citations])
    return to_markdown([*cols[:3], "Code", "Data", *cols[3:], "Paper", "Citations"], rows)


def open_rows(tables: list[dict], store: dict) -> list[dict]:
    return [i for t in tables if has_open(t) for e in t["entries"] if (i := open_info(e, store)) is not None]


def render_open_summary(data: dict, store: dict) -> str:
    rows = open_rows(data["tables"], store)
    if not rows:
        return "pending"
    return (f"of {len(rows):,} rows checked by {store['checked']}, {sum(map(has_code, rows)):,} have code, "
            f"{sum(map(has_data, rows)):,} have data or test files, {sum(has_code(r) and has_data(r) for r in rows):,} have both, "
            f"and nothing was found for {sum(map(found_nothing, rows)):,}")


def load_sections(by_id: dict) -> list[dict]:
    """One dict per templates/sections/*.md: number, title, template text, page path and its tables."""
    out = []
    for path in sorted(SECTION_TEMPLATES.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        number, title = re.match(r"# (\d+)\. (.+)", text).groups()
        out.append({"number": number, "title": title, "text": text, "page": SECTION_PAGES / path.name,
                    "tables": [by_id[t] for t in re.findall(r"<!-- TABLE:(t\d+) -->", text)]})
    return out


def page_link(section: dict) -> str:
    return f"{SECTION_PAGES.name}/{section['page'].name}"


def render_sections(sections: list[dict], store: dict) -> str:
    rows, total = [], [0, 0, 0, 0]
    for s in sections:
        found = open_rows(s["tables"], store)
        counts = [len(found), sum(map(has_code, found)), sum(map(has_data, found)), sum(map(found_nothing, found))]
        total = [a + b for a, b in zip(total, counts)]
        rows.append([f"[{s['number']}. {s['title']}]({page_link(s)})", *(f"{c:,}" for c in counts)])
    rows.append(["**Total**", *(f"**{c:,}**" for c in total)])
    return to_markdown(["Section", "Benchmarks", "With code", "With data", "Nothing found"], rows)


def render_widely_used(sections: list[dict], store: dict) -> str:
    rows = []
    for s in sections:
        for e in (e for t in s["tables"] for e in t["entries"] if "🔥" in e["cells"][0]):
            name, year, _, highlights = e["cells"][:4]
            info = open_info(e, store)
            rows.append([name, f"[{s['number']}]({page_link(s)})", year, highlights, code_words(info), data_words(info)])
    return to_markdown(["Benchmark", "Section", "Year / Venue", "Highlights", "Code", "Data"], rows)


def render_top_lists(data: dict, metrics: dict) -> str:
    cited, starred, seen_p, seen_r = [], [], set(), set()
    for _, e in iter_entries(data):
        name = plain_name(e["cells"][0])
        key = paper_key(e)
        p = metrics.get("papers", {}).get(key or "")
        if key and key not in seen_p and p and p.get("citations") is not None:
            seen_p.add(key)
            cited.append((p["citations"], name, p.get("url")))
        slug = resolve_repo(e, metrics)
        r = metrics.get("repos", {}).get(slug or "", {})
        if slug and slug not in seen_r and "stars" in r:
            seen_r.add(slug)
            starred.append((r["stars"], name, slug))
    if not cited and not starred:
        return ("_Citation and star rankings appear here after the first run of the "
                "[metrics workflow](.github/workflows/update-metrics.yml)._")
    cited.sort(key=lambda x: -x[0])
    starred.sort(key=lambda x: -x[0])
    rows = ["| # | Most cited | Citations | Most starred | Stars |", "|---|---|---|---|---|"]
    for i in range(min(TOP_N, max(len(cited), len(starred)))):
        c = cited[i] if i < len(cited) else None
        s = starred[i] if i < len(starred) else None
        c_cells = [c[1], f"[{c[0]:,}]({c[2]})" if c[2] else f"{c[0]:,}"] if c else ["", ""]
        s_cells = [f"[{s[1]}](https://github.com/{s[2]})", f"{s[0]:,}"] if s else ["", ""]
        rows.append(f"| {i + 1} | " + " | ".join(c_cells + s_cells) + " |")
    return "\n".join(rows)


def render() -> dict[Path, str]:
    data, metrics, store = load_data(), load_metrics(), load_open()
    by_id = {t["id"]: t for t in data["tables"]}
    sections = load_sections(by_id)
    out = {}
    for s in sections:
        text = s["text"]
        for t in s["tables"]:
            text = text.replace(f"<!-- TABLE:{t['id']} -->", render_benchmark_table(t, metrics, store))
        out[s["page"]] = (f"<!-- Generated by scripts/render_readme.py; edit data/benchmarks.yaml or {SECTION_TEMPLATES.parent.name}/"
                          f"{SECTION_TEMPLATES.name}/{s['page'].name} -->\n\n[← Overview and label guide](../README.md)\n\n" + text)
    text = TEMPLATE.read_text(encoding="utf-8")
    for table in data["tables"]:
        text = text.replace(f"<!-- TABLE:{table['id']} -->", render_table(table, metrics))
    text = text.replace("<!-- SECTIONS -->", render_sections(sections, store))
    text = text.replace("<!-- WIDELY_USED -->", render_widely_used(sections, store))
    text = text.replace("<!-- TOP_LISTS -->", render_top_lists(data, metrics))
    text = text.replace("<!-- OPEN_SUMMARY -->", render_open_summary(data, store))
    text = text.replace("<!-- METRICS_UPDATED -->", metrics.get("updated_at") or "pending first run")
    out[README] = text
    placed = [t["id"] for s in sections for t in s["tables"]]
    missing = [t["id"] for t in data["tables"] if has_open(t) and placed.count(t["id"]) != 1]
    if missing:
        sys.exit(f"tables that are not in exactly one section template: {missing}")
    return out


def main() -> None:
    files = render()
    stale = sorted(set(SECTION_PAGES.glob("*.md")) - set(files))
    if "--check" in sys.argv:
        old = [p.name for p, new in files.items() if not p.exists() or p.read_text(encoding="utf-8") != new]
        if old or stale:
            sys.exit(f"out of date: {', '.join(old + [p.name for p in stale])}: run `python scripts/render_readme.py`")
        return
    SECTION_PAGES.mkdir(exist_ok=True)
    for path, new in files.items():
        path.write_text(new, encoding="utf-8")
    print(f"rendered {len(files)} files" + (f"; no template for {', '.join(p.name for p in stale)}" if stale else ""))


if __name__ == "__main__":
    main()
