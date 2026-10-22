"""Lab 01: log analyzer. Implement the functions, then run: pytest -q"""
from __future__ import annotations

from typing import Iterable


def parse_line(line: str) -> dict | None:
    """Parse '2026-10-26T10:00:01Z INFO GET /health 200 12ms'.

    Return {"ts": str, "level": str, "method": str, "path": str, "status": int, "ms": int},
    or None if the line is malformed (wrong field count, non-numeric status,
    or latency not of the form '<digits>ms').
    """
    raise NotImplementedError


def summarize(lines: Iterable[str]) -> dict:
    """Return {"total", "malformed", "by_level", "error_rate", "p95_ms", "top_paths"}.

    - total: number of valid lines; malformed: number of invalid (non-empty or empty) lines
    - by_level: {level: count} over valid lines
    - error_rate: share of valid lines with status >= 500 (0.0 if none)
    - p95_ms: nearest-rank percentile of latency: sorted values, index ceil(0.95 * n) - 1 (0 if none)
    - top_paths: up to 3 (path, count) pairs, count descending then path ascending
    """
    raise NotImplementedError
