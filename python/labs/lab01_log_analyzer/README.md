# Lab 01: Log analyzer

## Goal

Turn access-log lines into a predictable summary without crashing on malformed input.

**Input format:** `2026-10-26T10:00:01Z INFO GET /health 200 12ms` — six space-separated fields: timestamp, level, method, path, status, latency.

## Build

Implement `parse_line` and `summarize` in `analyzer.py`. Use the docstrings as the behavioural contract; do not silently change the return shape.

1. Read `sample.log` and list the valid and invalid line cases before coding.
2. Implement `parse_line`: return the documented dictionary for valid records and `None` for malformed records.
3. Implement `summarize`: count valid/malformed lines, count levels, calculate the HTTP 5xx error rate, compute nearest-rank p95 latency, and rank up to three paths by count (ties sorted by path).
4. Add at least one test not already covered, such as whitespace-only input, a zero-millisecond latency, a 404 that must not count as a 5xx error, or a tie in top-path counts.
5. Optional stretch: add `python analyzer.py sample.log` that prints a stable JSON summary. Keep the core functions independently testable.

## Verify

From this directory:

```bash
python -m pytest -q
```

The supplied tests cover valid parsing, malformed records, basic summary counts, nearest-rank p95, and empty input. A passing suite does not prove your extra edge case is correct unless you added and ran that test yourself.

## Evidence to record

- The exact test command and result.
- One new edge-case test and why it matters.
- A short explanation of why the p95 index is `ceil(0.95 * n) - 1`.
- One limitation of this parser (for example, its intentionally simple space-delimited format).

Do not mark the lab complete until you can explain the error-rate denominator and reproduce the tests from a clean checkout.
