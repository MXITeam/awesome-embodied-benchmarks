"""Shared helpers for the metrics updater and README renderer."""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "benchmarks.yaml"
METRICS = ROOT / "data" / "metrics.json"
TEMPLATE = ROOT / "templates" / "README.template.md"
README = ROOT / "README.md"


def load_data() -> dict:
    return yaml.safe_load(DATA.read_text(encoding="utf-8"))


def load_metrics() -> dict:
    if METRICS.exists():
        return json.loads(METRICS.read_text(encoding="utf-8"))
    return {"updated_at": None, "papers": {}, "repos": {}, "discovered_github": {}}


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
