# NSE Insights Platform

**Mission:** give Kenyan NSE investors timely, trustworthy, plain-language news and context per stock: one place, updated daily to hourly. Built by you, run as a business.

**Positioning:** faster, clearer *information*, not predictions and not personal investment advice. Predictive modelling is a stretch goal and never the headline claim.

## Free supporting resources

Use the [free-first resource guide](../docs/RESOURCE_GUIDE.md#nse-market-insights-platform) for pandas, FastAPI, SQLAlchemy, and PostgreSQL learning material mapped to this project. Keep the project's [data-source inventory](DATA_SOURCES.md), [evaluation plan](EVAL.md), and [compliance notes](COMPLIANCE.md) authoritative for provider terms and evaluation claims.

## Phases (see `PHASES.md`)
1. **Aggregator** (Weeks 1–4): prices + news ingestion, ticker tagging, storage, read API
2. **Insight** (Weeks 5–8): LLM summaries, sentiment/risk flags, daily brief, delivery prototype
3. **Commercial** (after assessments): pricing, distribution, public trading journey (`journey/`)

Weeks 9–16: maintenance only (≤ 1h/week). Protect the assessment prep.

## Layout
- `src/nse_insights/`: Python package (seed code + tests included)
- `schema.sql`: Postgres schema
- `ARCHITECTURE.md`, `DATA_SOURCES.md`, `COMPLIANCE.md`, `EVAL.md`, `PHASES.md`
- `journey/`: public trading-journey plan, rules, templates

```bash
cd nse_platform && python -m pytest -q
```
