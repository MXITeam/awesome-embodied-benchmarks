"""Fetch citation counts and GitHub stars for every benchmark in data/benchmarks.yaml.

Sources
  * Citations: Semantic Scholar Graph API (batch by arXiv id, title match otherwise);
               OpenAlex as a fallback for arXiv papers Semantic Scholar does not know yet.
  * Code repos: `github:` field in the YAML; otherwise discovered from the Hugging Face
               Papers API (`githubRepo`) or a github.com link in the arXiv abstract/comment.
  * Stars:    GitHub REST API (uses GITHUB_TOKEN when available).

Previous values in data/metrics.json are kept when a source is unavailable, so a
flaky API never wipes numbers from the README.

Env vars (all optional): GITHUB_TOKEN, S2_API_KEY.
"""
from __future__ import annotations

import datetime as dt
import difflib
import os
import re
import sys
import time
import xml.etree.ElementTree as ET

import requests

from common import iter_entries, load_data, load_metrics, normalize_repo, paper_key, plain_name, save_metrics

S2 = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,citationCount,externalIds,url"
UA = {"User-Agent": "awesome-embodied-benchmarks-metrics-bot"}

session = requests.Session()
session.headers.update(UA)


def s2_headers() -> dict:
    key = os.environ.get("S2_API_KEY")
    return {"x-api-key": key} if key else {}


def request(method: str, url: str, *, tries: int = 5, **kw) -> requests.Response | None:
    delay = 3.0
    for attempt in range(tries):
        try:
            r = session.request(method, url, timeout=30, **kw)
        except requests.RequestException as exc:
            print(f"  ! {method} {url}: {exc}", file=sys.stderr)
            r = None
        if r is not None and r.status_code not in (429, 500, 502, 503, 504):
            return r
        time.sleep(delay)
        delay *= 2
    return r


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def title_ok(entry: dict, found: str) -> bool:
    """Accept a title-search hit only if it really is the paper we listed."""
    want = entry.get("title", "")
    if difflib.SequenceMatcher(None, norm_title(want), norm_title(found)).ratio() >= 0.8:
        return True
    alias = entry.get("match") or plain_name(entry["cells"][0]).split(" / ")[0].split(" (")[0]
    return norm_title(alias) in norm_title(found)


# --------------------------------------------------------------------------- citations
def fetch_citations(entries: list[dict], metrics: dict) -> None:
    papers = metrics.setdefault("papers", {})
    today = dt.date.today().isoformat()

    arxiv_ids = sorted({e["arxiv"] for e in entries if e.get("arxiv")})
    for i in range(0, len(arxiv_ids), 400):
        chunk = arxiv_ids[i : i + 400]
        r = request("POST", f"{S2}/paper/batch", params={"fields": S2_FIELDS},
                    json={"ids": [f"ARXIV:{a}" for a in chunk]}, headers=s2_headers())
        if r is None or r.status_code != 200:
            print(f"  ! S2 batch failed: {getattr(r, 'status_code', 'n/a')}", file=sys.stderr)
            continue
        for aid, hit in zip(chunk, r.json()):
            if hit and hit.get("citationCount") is not None:
                papers[f"arXiv:{aid}"] = {"citations": hit["citationCount"], "url": hit.get("url"),
                                          "title": hit.get("title"), "arxiv": aid, "source": "semanticscholar",
                                          "checked": today}

    # OpenAlex fallback for arXiv papers S2 has not indexed yet
    for aid in arxiv_ids:
        p = papers.get(f"arXiv:{aid}")
        if p and p.get("source") == "semanticscholar" and p.get("checked") == today:
            continue
        r = request("GET", f"https://api.openalex.org/works/https://doi.org/10.48550/arXiv.{aid}", tries=2)
        if r is not None and r.status_code == 200:
            w = r.json()
            papers[f"arXiv:{aid}"] = {"citations": w.get("cited_by_count", 0), "url": w.get("id"),
                                      "title": w.get("display_name"), "arxiv": aid, "source": "openalex",
                                      "checked": today}
        time.sleep(0.2)

    # title-only entries
    for e in entries:
        if e.get("arxiv") or not e.get("title"):
            continue
        key = paper_key(e)
        r = request("GET", f"{S2}/paper/search/match", params={"query": e["title"], "fields": S2_FIELDS},
                    headers=s2_headers(), tries=3)
        time.sleep(1.1 if not os.environ.get("S2_API_KEY") else 0.2)
        if r is None or r.status_code != 200:
            continue
        data = r.json().get("data") or []
        if not data or not title_ok(e, data[0].get("title", "")):
            print(f"  ? no confident match for {e['title']!r}", file=sys.stderr)
            continue
        hit = data[0]
        papers[key] = {"citations": hit.get("citationCount") or 0, "url": hit.get("url"), "title": hit.get("title"),
                       "arxiv": (hit.get("externalIds") or {}).get("ArXiv"), "source": "semanticscholar",
                       "checked": today}


# --------------------------------------------------------------------------- repos
def discover_repos(entries: list[dict], metrics: dict) -> None:
    found = metrics.setdefault("discovered_github", {})
    papers = metrics.get("papers", {})
    targets = {}
    for e in entries:
        if e.get("github") or e.get("no_github"):
            continue
        key = paper_key(e)
        aid = e.get("arxiv") or (papers.get(key) or {}).get("arxiv") if key else None
        if key and aid and key not in found:
            targets[key] = aid
    if not targets:
        return

    # 1) Hugging Face Papers API
    for key, aid in targets.items():
        r = request("GET", f"https://huggingface.co/api/papers/{aid}", tries=2)
        if r is not None and r.status_code == 200:
            slug = normalize_repo(r.json().get("githubRepo"))
            if slug:
                found[key] = slug
        time.sleep(0.2)

    # 2) github.com link in arXiv abstract / comment
    rest = {k: a for k, a in targets.items() if k not in found}
    ids = list(rest.values())
    for i in range(0, len(ids), 50):
        chunk = ids[i : i + 50]
        r = request("GET", "https://export.arxiv.org/api/query",
                    params={"id_list": ",".join(chunk), "max_results": len(chunk)}, tries=3)
        if r is None or r.status_code != 200:
            continue
        ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
        for item in ET.fromstring(r.content).findall("a:entry", ns):
            aid = re.sub(r"v\d+$", "", item.findtext("a:id", "", ns).rsplit("/", 1)[-1])
            text = " ".join(filter(None, [item.findtext("a:summary", "", ns), item.findtext("x:comment", "", ns)]))
            m = re.search(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", text)
            if m:
                slug = normalize_repo(m.group(1).rstrip("."))
                for k, a in rest.items():
                    if a == aid and slug:
                        found[k] = slug
        time.sleep(3)


def fetch_stars(entries: list[dict], metrics: dict) -> None:
    repos = metrics.setdefault("repos", {})
    found = metrics.get("discovered_github", {})
    headers = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    slugs = set()
    for e in entries:
        slug = normalize_repo(e.get("github")) or found.get(paper_key(e) or "")
        if slug:
            slugs.add(slug)
    today = dt.date.today().isoformat()
    for slug in sorted(slugs):
        r = request("GET", f"https://api.github.com/repos/{slug}", headers=headers, tries=3)
        if r is None:
            continue
        if r.status_code == 404:
            print(f"  ! repo not found: {slug}", file=sys.stderr)
            repos[slug] = {"missing": True, "checked": today}
            continue
        if r.status_code != 200:
            continue
        j = r.json()
        repos[slug] = {"stars": j["stargazers_count"], "full_name": j["full_name"], "url": j["html_url"],
                       "archived": j.get("archived", False), "checked": today}


def main() -> None:
    data = load_data()
    metrics = load_metrics()
    entries = [e for _, e in iter_entries(data)]
    print(f"{len(entries)} entries")
    print("· citations"); fetch_citations(entries, metrics)
    print("· repo discovery"); discover_repos(entries, metrics)
    print("· stars"); fetch_stars(entries, metrics)
    metrics["updated_at"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    save_metrics(metrics)
    n_c = sum(1 for p in metrics["papers"].values() if p.get("citations") is not None)
    n_s = sum(1 for r in metrics["repos"].values() if "stars" in r)
    print(f"done: {n_c} papers with citations, {n_s} repos with stars")


if __name__ == "__main__":
    main()
