# Lab 01: Log analyzer
Format: `2026-10-26T10:00:01Z INFO GET /health 200 12ms` (6 space-separated fields).
Implement `parse_line` and `summarize` in `analyzer.py`. Run `pytest -q`.
Stretch: add a CLI (`python analyzer.py sample.log`) that prints the summary as JSON.
