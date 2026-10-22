# Python curriculum

| Wk | Theme | Lab / deliverable |
|---|---|---|
| 1 | Fundamentals audit: typing, dataclasses, comprehensions, generators, context managers, exceptions, `pyproject.toml` | **lab01** log analyzer |
| 2 | Files/JSON/CSV, `pathlib`, `argparse`, `logging`, pytest | **lab02** retry decorator; build a CLI that wraps lab01 |
| 3 | HTTP (`httpx`), HTML parsing, retries, rate limiting, async basics | **lab04** price parser; fetch one real page politely (check ToS/robots) |
| 4 | FastAPI + Pydantic + SQLite → Postgres | **lab03** notes API; then persist to SQLite |
| 5 | JWT auth, input validation, rate limiting, API tests | secure the notes API (authn/authz, validation, limits) |
| 6 | NumPy/pandas fluency, data cleaning, SQL basics | clean a messy CSV of prices; groupby/rolling returns |
| 7 | pytest advanced (fixtures, parametrize, mocking), packaging, mypy/ruff | add CI to a lab |
| 8 | AWS/boto3 (S3, Lambda), automation scripts | upload a daily brief to S3 from a script |
| 9 | Concurrency: threads vs processes vs asyncio, profiling | speed up a fetcher 5×; explain the GIL |
| 10 | Interview core: OOP, decorators, closures, iterators, memory model, mutability | answer `assessments/interview/python.md` aloud |
| 11 | SQL for assessments: joins, GROUP BY, windows, CTEs | 30 SQL problems, timed |
| 12 | DevOps scripting: `subprocess`, log parsing, health checks | a deploy-check script with exit codes |
| 13–16 | Assessment-style timed Python + SQL; fix weak spots from the log | weekly timed set |

## Labs 05+ (spec only, you build them)
- **lab05 CLI tool**: `typer`/`argparse` tool that tails a log, filters by level, outputs JSON; packaged with an entry point.
- **lab06 async fetcher**: fetch 50 URLs with a concurrency limit, timeouts, retries with jitter; test with a fake server.
- **lab07 SQLite repository**: CRUD with parameterised queries; migration script; tests with an in-memory DB.
- **lab08 JWT middleware**: sign/verify tokens, expiry, role check; negative tests for tampering.
- **lab09 S3 uploader**: boto3 with a stubbed client; idempotent uploads; checksum.
- **lab10 pipeline runner**: tiny DAG executor with retries and a dry-run mode.

## Must be able to explain (without notes)
mutable default arguments · list vs tuple vs set vs dict internals · generators & `yield` · decorators & `functools.wraps` · `__init__` vs `__new__` · GIL and when threads help · `is` vs `==` · shallow vs deep copy · context managers · `*args/**kwargs` · type hints are not enforced at runtime · how `dict` preserves order · why `list.pop(0)` is slow.
