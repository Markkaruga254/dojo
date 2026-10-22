# Architecture (v1)

```
 sources ──► ingestors (Python) ──► raw store ──► processors ──► Postgres ──► FastAPI ──► web / email / WhatsApp
 (prices,     scheduled, idempotent    (html/json     dedupe,        prices,       read API     briefs
  news RSS,                            snapshots)     ticker tags,   news,
  filings)                                            LLM summary,   summaries,
                                                      risk flags     flags
```

Principles
- **Idempotent ingest:** re-running a job never duplicates rows (unique keys: `ticker+day`, canonical URL).
- **Keep raw data** so processors can be re-run when prompts/models change.
- **Every LLM output stores** model, prompt version, input hash, timestamp.
- **Cost caps** per day; summaries cached by content hash.
- **Degrade gracefully:** if a source is down, serve stale data with a visible "as of" time.
- **Secrets in env/secret manager,** never in git.

Stack (starter): Python 3.12, `httpx`, `beautifulsoup4`/`feedparser`, Postgres, SQLAlchemy or `psycopg`, FastAPI, Docker, GitHub Actions → a managed container service. Start with SQLite locally if Postgres slows you down.
