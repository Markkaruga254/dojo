# NSE Insights Platform

**Mission:** give Kenyan NSE investors timely, trustworthy, plain-language news and context per stock: one place, updated daily to hourly. Built by you, run as a business.

**Positioning:** faster, clearer *information*, not predictions and not personal investment advice. Predictive modelling is a stretch goal and never the headline claim.

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
