# Lab 03: Notes API (FastAPI)

## Goal

Build a small HTTP API with explicit status codes, input validation, predictable ordering, and useful not-found behavior. Start with in-memory storage so the HTTP contract is clear before adding persistence.

## Prerequisites

Install the optional lab dependencies from the repository root:

```bash
python -m pip install -e ".[labs]"
```

This installs the project's optional FastAPI and HTTPX dependencies; pytest is included by the `dev` extra.

## Build

Implement the TODO endpoints in `app.py`:

- `POST /notes`: return 201 and the created note as `{"id", "title", "body"}`.
- `GET /notes/{id}`: return 200 and the note, or 404 if it does not exist.
- `GET /notes`: return 200 with notes ordered by ID.
- `DELETE /notes/{id}`: return 204 with an empty response body, or 404 if it does not exist.
- Keep the `NoteIn` validation: title is required and must contain 1–100 characters.

Use the supplied in-memory store for the first pass. Do not add SQLite, authentication, pagination, or Docker until the required contract passes.

## Verify

From this directory:

```bash
python -m pytest -q
```

The tests exercise create/read, ordering, missing IDs, delete semantics, and invalid input. Add at least one test of your own, such as whitespace-only titles, ID allocation after deletion, or listing an empty store. Decide and document whether a whitespace-only title should be valid; the current minimum-length validation does not trim whitespace automatically.

## Explain and record

- Why creation returns 201 and successful deletion returns 204.
- Why the API returns 404 rather than an empty object for a missing ID.
- What in-memory storage loses when the process restarts and what concurrency/persistence concerns it leaves unresolved.
- The exact test command, result, and added edge-case test.

## Stretch sequence

1. Replace the dictionary with SQLite while preserving the HTTP contract.
2. Add authentication and tests that prove users cannot read or delete another user's notes.
3. Add pagination with a stable ordering.
4. Containerise the service and document how to run and stop it.

Do not expose a real notes service publicly before authentication, authorisation, and data-handling behavior have been reviewed.
