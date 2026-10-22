# Phases and acceptance criteria

## Phase 1: Aggregator (W1–4)
- [ ] Data-source audit written (`DATA_SOURCES.md` filled with verified terms)
- [ ] Prices for a defined universe (start with ~10 liquid tickers) ingested daily, idempotent
- [ ] News from ≥ 3 sources ingested, deduplicated by canonical URL, tagged to tickers
- [ ] Runs unattended 7 days (scheduler: cron/GitHub Actions to start)
- [ ] Postgres storage + read API (`/tickers`, `/tickers/{t}/prices`, `/tickers/{t}/news`)
- [ ] Health endpoint + a "last successful ingest" metric

## Phase 2: Insight (W5–8)
- [ ] Entity linking improved (aliases, subsidiaries), event types: earnings, dividends, rights/IPO, governance, regulatory, political risk
- [ ] LLM summaries with caching, token/cost caps, prompt versioning
- [ ] 100-item hand-labelled eval set; sentiment/risk flag precision reported (`EVAL.md`)
- [ ] Daily brief per ticker and a market-wide brief, generated automatically
- [ ] Delivery prototype (email first; WhatsApp Business API later)

## Phase 3: Commercial (after mid-Feb)
- [ ] Legal/compliance check done (`COMPLIANCE.md`)
- [ ] Free tier (daily digest) + paid tier (alerts, deeper briefs, API) defined
- [ ] 20 beta users from investment clubs / SACCOs; feedback loop weekly
- [ ] Public 30-day trading journey (`journey/PLAN.md`)
