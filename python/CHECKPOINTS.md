# Applied Python checkpoints

A lab is complete when you can explain its design, pass the tests, add a meaningful edge-case test, and reproduce the result from a clean checkout. Merely making starter tests pass is not enough.

## Lab completion checklist

- [ ] Read the lab brief and list expected behaviour before coding.
- [ ] Add at least one test for an edge case not already shown.
- [ ] Implement in small steps; keep functions focused and names meaningful.
- [ ] Run the lab tests and relevant lint/type checks documented by the lab.
- [ ] Explain the main design choice and one alternative.
- [ ] Record any hint or AI assistance honestly and reproduce the solution without copying.

## Milestones

| Milestone | Practical demonstration | Evidence |
|---|---|---|
| Python fundamentals | Parse a log safely; handle malformed lines and missing fields without crashing | Lab tests plus an additional edge-case test |
| Files and CLI | Build a command that reads input, reports errors with useful exit codes, and emits predictable output | CLI invocation, fixture input, and expected output |
| HTTP and retries | Fetch a permitted public endpoint politely; handle timeout, status errors, and retry limits | Mocked tests; no live-service dependency for normal CI |
| API and persistence | Implement validated request/response models and parameterised database operations | Tests for valid, invalid, unauthorised, and boundary requests |
| Data and SQL | Clean a small dataset, explain missing-value choices, and write joins/aggregations without target leakage | Reproducible script, SQL queries, and short explanation |
| Engineering quality | Refactor a lab into understandable modules and keep tests deterministic | Test output, lint output, and brief design note |
| Interview readiness | Solve a Python task under a timer, then explain mutability, iterators, decorators, exceptions, and complexity | Timed attempt plus retrospective |

## Exit interview

Without notes, explain:

1. What happens when an exception is raised and not caught?
2. When is a generator preferable to a list?
3. What is the difference between identity and equality in Python?
4. Why are mutable default arguments risky?
5. When does concurrency help I/O-bound work, and what are its limits?
6. How would you test retry logic without making real network requests?
7. How do parameterised SQL queries prevent injection?

A strong answer includes a small example and a trade-off, not just a definition.

## Resource boundaries

Some labs need optional dependencies. Install only what the chosen lab documents. Do not require paid APIs for the normal learning path; use mocked network clients for deterministic tests and check terms before fetching external data.
