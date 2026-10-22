# Applied Python track

Python that ML, backend and DevOps roles actually test: clean code, tests, HTTP/APIs, data handling, concurrency, scripting for automation, SQL, and the language's sharp edges.

## Learning path

- CURRICULUM.md: week-by-week themes, lab specs, and the "must be able to explain" list.
- labs/: test-backed labs. Starter code may raise NotImplementedError; implement the requested behaviour and run the lab tests.
- CHECKPOINTS.md: milestone demonstrations and a no-notes exit interview.

Run one lab at a time:

```bash
make lab LAB=lab01_log_analyzer
# Or:
cd python/labs/lab01_log_analyzer
python -m pytest -q
```

## Free supporting resources

Use the [free-first resource guide](../docs/RESOURCE_GUIDE.md#applied-python) for the official Python tutorial, free structured lessons, pytest documentation, and optional exercises. Choose the resource that addresses the current lab blocker, then return to the lab and add an edge-case test.

## Working rules

1. Read the brief and docstrings before editing.
2. Write an extra test for an edge case before implementation.
3. Make the smallest change that satisfies the behaviour.
4. Run the lab tests and relevant lint checks.
5. Explain the design choice and one alternative in your own words.
6. Ask for review after you have attempted the work; do not copy a full solution from AI.

A lab is not evidence of mastery until you can explain it and reproduce the result. Use [Python checkpoints](CHECKPOINTS.md) to assess independence.
