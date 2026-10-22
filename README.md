# Forge-90

**One repo. One daily system. 16 weeks (26 Oct 2026 → 14 Feb 2027) to become interview-ready
as a software / ML / DevOps engineer while shipping a real product.**

> Working name. Before you push, check `github.com/<you>/forge-90` is free (or rename the folder).

## What this replaces
Three separate learning threads are merged here: the 90-day ML capstone, the Python/DevOps/cloud
coursebook, and daily Python + DSA interview prep. The NSE investor-insights platform is the
applied project that the Python and ML tracks feed.

## The five tracks
| Track | Folder | What it builds |
|---|---|---|
| DSA | `dsa/` | LeetCode-style fluency from zero: patterns, curated ~150 problems, spaced re-solves |
| Applied Python | `python/` | Python for ML, backend, DevOps and cloud, with test-backed labs |
| ML | `ml/` | Hugging Face tracks A–F, from-scratch labs, legal-access capstone |
| Platform | `nse_platform/` | NSE news/price aggregator → sentiment & daily briefs → commercial product |
| Cloud/DevOps | `cloud/` | Containers, CI/CD, Terraform, security overlay, Cloud Track teaching plan |

Plus `assessments/` (mock tests, rubrics, interview banks) and `log/` (your daily record, the centre of the system).

## Start in 15 minutes
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev,labs]"
make test          # forge CLI tests should pass
make day           # creates today's log from the template
make week          # shows this week's focus
```

## Daily loop
1. `make day` → open today's log.
2. Run the blocks in `docs/DAILY_PROTOCOL.md` (DSA → Python → ML → Platform → log).
3. Record every DSA attempt: `python scripts/forge.py problem "Two Sum" --topic arrays --difficulty easy --mode independent --minutes 18 --result solved`
4. Shut down with the log review. Plan tomorrow's top 3.
5. `make stats` every Sunday.

## Non-negotiables
- **Independent / hinted / assisted** is logged honestly. It is the only metric that matters.
- Attempt before AI. AI clarifies and reviews your work; it does not hide gaps.
- Gates are objective (`ROADMAP.md`). You do not move on by feeling.
- One lighter block per week and one real rest day. Burnout is the main risk to this plan.

## Map
`ROADMAP.md` · `docs/PRINCIPLES.md` · `docs/DAILY_PROTOCOL.md` · `docs/ASSESSMENT_STRATEGY.md` ·
`docs/HF_SYLLABUS_CHECK.md` · `docs/TOOLS_SETUP.md` · `config/plan.json` (single source of truth for weekly focus)

## Verified vs not verified (when this repo was generated)
- Tests run and passing against reference solutions: forge CLI, DSA pattern snippets, Python labs 01/02/04, ML labs 01/02, platform seed module.
- **Not executed at generation time** (no network): `python/labs/lab03_notes_api` (needs FastAPI), `ruff`, the GitHub Actions workflow. Run `make test` and push once to confirm CI.
- Hugging Face chapter mapping is intentionally blank: fill it in Week 1.
