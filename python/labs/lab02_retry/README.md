# Lab 02: Retry decorator

## Goal

Build a reusable retry decorator that retries only selected exceptions and can be tested without waiting through real delays.

## Build

Implement `retry` in `retry.py` with:

- exponential backoff and a configurable attempt limit (`times` is the total number of attempts, including the first call);
- a configurable tuple of retryable exception types;
- injectable `sleep` so tests can capture delays without sleeping;
- `functools.wraps` so the wrapped function keeps its metadata;
- propagation of non-retryable exceptions and the final failure after retries are exhausted.

Use the function signature and docstrings in the starter file as the source of truth for exact parameter names and retry-count semantics.

## Verify

From this directory:

```bash
python -m pytest -q
```

Add tests for a function that succeeds after a transient failure, a non-retryable exception, exhausted retries, the recorded backoff sequence, and preserved function metadata. Mock or inject sleep; tests should not depend on wall-clock delays.

## Explain and record

- Why `times=3` means three total attempts, not one initial call plus three retries.
- Why only selected exceptions should be retried.
- How exponential backoff helps and when jitter is useful.
- The test command, result, and one edge case you added.

Stretch: add jitter with an injectable or seedable random source so tests remain deterministic. Avoid retrying non-idempotent operations without understanding the risk of duplicate side effects.
