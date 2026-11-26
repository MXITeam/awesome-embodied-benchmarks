# Contributing

Thanks for helping keep this list comprehensive and accurate!

`README.md` (the overview) and `benchmarks/*.md` (one page per section, with the full tables) are **generated** — please don't edit them by hand. Edit these instead:

| File | What lives there |
|---|---|
| [`data/benchmarks.yaml`](data/benchmarks.yaml) | Every table row (the source of truth) |
| [`templates/README.template.md`](templates/README.template.md) | Overview prose, leaderboard, platform and dataset sections |
| [`templates/sections/*.md`](templates/sections) | Title, intro and `<!-- TABLE:tNN -->` placeholder of each benchmark section; `templates/sections/NN-slug.md` renders to `benchmarks/NN-slug.md` |
| `data/metrics.json` | Citations / stars cache — written by the bot, don't edit |
| `data/open_source.json` | Code / data availability of each row — matched by script, partly checked by hand |

## Adding a benchmark

Add an entry under the right table in `data/benchmarks.yaml`:

```yaml
  - cells:
    - 🆕 **MyBench**            # Name (🆕 = released this year, 🔥 = de-facto standard)
    - 2026 / CoRL               # Year / Venue
    - Sim (MuJoCo)              # Type: Sim, Real, Real2Sim, World model, QA …
    - 40 tasks; one-line highlight of what makes it distinct
    arxiv: '2601.01234'         # preferred — drives the Paper link and citation count
    github: owner/repo          # optional — auto-discovered from HF/arXiv if omitted
```

Other optional fields:

- `title:` — exact paper title, when there is no arXiv ID (citations are then matched by title).
- `match:` — a word that must appear in the matched title (guards against wrong title matches).
- `link:` — custom markdown for the Paper column (e.g. a venue page).
- `code:` / `data:` — URL of the code or of the data / test files; overrides `data/open_source.json`.
- `no_paper: true` — row has no paper to track (platforms, notes).

Then preview locally:

```bash
pip install -r scripts/requirements.txt
python scripts/render_readme.py              # offline render of README.md and benchmarks/*.md
python scripts/render_readme.py --check      # fails when a generated file is out of date
python scripts/update_metrics.py             # optional: refresh citations/stars (needs network)
```

Guidelines: put a benchmark in the most specific category (at most two sections), keep rows sorted by year, and one line of highlights is enough.
