"""Shared helpers for the metrics updater and README renderer."""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "benchmarks.yaml"
METRICS = ROOT / "data" / "metrics.json"
OPEN = ROOT / "data" / "open_source.json"
TEMPLATE = ROOT / "templates" / "README.template.md"
README = ROOT / "README.md"
SECTION_TEMPLATES = ROOT / "templates" / "sections"
SECTION_PAGES = ROOT / "benchmarks"


def load_data() -> dict:
    return yaml.safe_load(DATA.read_text(encoding="utf-8"))


def load_metrics() -> dict:
    if METRICS.exists():
        return json.loads(METRICS.read_text(encoding="utf-8"))
    return {"updated_at": None, "papers": {}, "repos": {}, "discovered_github": {}}


def load_open() -> dict:
    """Code / data availability per row, keyed by paper_key() or "name:<row name>"."""
    if OPEN.exists():
        return json.loads(OPEN.read_text(encoding="utf-8"))
    return {"checked": None, "rows": {}}


def has_open(table: dict) -> bool:
    """Benchmark tables carry the Code and Data columns; platform, dataset-pointer, survey and starter tables do not."""
    return "Highlights" in table["columns"]


def open_info(entry: dict, store: dict) -> dict | None:
    """Availability of one row; `code:` / `data:` URLs in benchmarks.yaml win over the JSON. None = not checked."""
    info = store["rows"].get(paper_key(entry) or "name:" + plain_name(entry["cells"][0]))
    if entry.get("code"):
        info = {**(info or {"data": "unchecked"}), "code": "code", "code_url": entry["code"]}
    if entry.get("data"):
        info = {**(info or {"code": "unchecked"}), "data": "download", "data_url": entry["data"]}
    return info


DATA_FOUND = ("download", "request", "in_repo", "script", "hf_named")


def has_code(info: dict) -> bool:
    return info.get("code") == "code"


def has_data(info: dict) -> bool:
    return info.get("data") in DATA_FOUND


def found_nothing(info: dict) -> bool:
    """No code, no data, no project page and no announcement."""
    return (info.get("code") in (None, "gone") and not has_data(info) and info.get("data") not in ("claim", "promise"))


CODE_WORDS = {"code": "Code", "no_code_in_repo": "Repo without code", "anonymous_repo": "Anonymous repo",
              "project_page": "Project page", "claimed": "Announced", "promised": "Announced", "gone": "Dead link", "unchecked": ""}
DATA_WORDS = {"download": "Download", "request": "On request", "hf_named": "Same-name dataset (unverified)", "in_repo": "In repo",
              "script": "Download script", "code_only": "Tasks in code", "claim": "Announced", "promise": "Announced", "unchecked": ""}
LICENSE_WORDS = {"none": "no license", "license file, type not identified": "license file"}


def _link(words: str | None, url: str | None) -> str:
    return f"[{words}]({url})" if words and url else ("Not found" if words is None else words)


def code_words(info: dict | None) -> str:
    return _link(CODE_WORDS.get(info.get("code")), info.get("code_url")) if info else ""


def data_words(info: dict | None) -> str:
    return _link(DATA_WORDS.get(info.get("data")), info.get("data_url")) if info else ""


def license_words(info: dict | None) -> str:
    lic = info.get("license") if info and has_code(info) else None
    return LICENSE_WORDS.get(lic, lic) if lic else ""


def save_metrics(m: dict) -> None:
    METRICS.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def plain_name(name_md: str) -> str:
    m = re.search(r"\*\*(.+?)\*\*", name_md)
    return (m.group(1) if m else name_md).strip()


def paper_key(entry: dict) -> str | None:
    """Stable key identifying the paper behind an entry (None = no paper to track)."""
    if entry.get("no_paper"):
        return None
    if entry.get("arxiv"):
        return f"arXiv:{entry['arxiv']}"
    if entry.get("title"):
        return f"title:{entry['title']}"
    return None


def iter_entries(data: dict):
    for table in data["tables"]:
        if table.get("metrics", True) is False:
            continue
        for entry in table["entries"]:
            yield table, entry


def normalize_repo(url_or_slug: str | None) -> str | None:
    if not url_or_slug:
        return None
    m = re.search(r"(?:github\.com/)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?:\.git)?/?$", url_or_slug.strip())
    if not m:
        return None
    slug = m.group(1)
    if slug.lower().endswith((".github.io",)) or slug.count("/") != 1:
        return None
    return slug
