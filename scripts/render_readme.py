"""Render README.md from templates/README.template.md + data/benchmarks.yaml + data/metrics.json.

Runs offline; network access is only needed by update_metrics.py.
Use `--check` in CI to fail when README.md is out of date.
"""
from __future__ import annotations

import sys
import urllib.parse

from common import README, TEMPLATE, iter_entries, load_data, load_metrics, normalize_repo, paper_key, plain_name

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


def render_table(table: dict, metrics: dict) -> str:
    cols = list(table["columns"])
    with_metrics = table.get("metrics", True)
    header = cols + (["Paper", "Citations", "GitHub ⭐"] if with_metrics else [])
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for e in table["entries"]:
        cells = list(e["cells"]) + [""] * (len(cols) - len(e["cells"]))
        if with_metrics:
            if e.get("no_paper") and not e.get("link") and not e.get("github"):
                cells += ["", "", ""]
            else:
                cells += [paper_cell(e, metrics), citation_cell(e, metrics), stars_cell(e, metrics)]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


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


def render() -> str:
    data = load_data()
    metrics = load_metrics()
    text = TEMPLATE.read_text(encoding="utf-8")
    for table in data["tables"]:
        text = text.replace(f"<!-- TABLE:{table['id']} -->", render_table(table, metrics))
    text = text.replace("<!-- TOP_LISTS -->", render_top_lists(data, metrics))
    text = text.replace("<!-- METRICS_UPDATED -->", metrics.get("updated_at") or "pending first run")
    return text


def main() -> None:
    new = render()
    if "--check" in sys.argv:
        if README.read_text(encoding="utf-8") != new:
            sys.exit("README.md is out of date: run `python scripts/render_readme.py`")
        return
    README.write_text(new, encoding="utf-8")
    print("README.md rendered")


if __name__ == "__main__":
    main()
