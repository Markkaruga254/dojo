import pytest
from analyzer import parse_line, summarize


def test_parse_valid():
    assert parse_line("2026-10-26T10:00:01Z INFO GET /health 200 12ms") == {
        "ts": "2026-10-26T10:00:01Z", "level": "INFO", "method": "GET",
        "path": "/health", "status": 200, "ms": 12,
    }


@pytest.mark.parametrize("bad", [
    "", "garbage", "2026-10-26T10:00:01Z INFO GET /x abc 12ms",
    "2026-10-26T10:00:01Z INFO GET /x 200 12", "2026-10-26T10:00:01Z INFO GET /x 200 12ms extra",
])
def test_parse_malformed(bad):
    assert parse_line(bad) is None


def test_summary_basic_counts():
    lines = [
        "2026-10-26T10:00:01Z INFO GET /a 200 10ms",
        "2026-10-26T10:00:02Z INFO GET /b 200 20ms",
        "2026-10-26T10:00:03Z ERROR GET /a 500 30ms",
        "2026-10-26T10:00:04Z WARN POST /c 429 40ms",
        "oops",
    ]
    s = summarize(lines)
    assert s["total"] == 4 and s["malformed"] == 1
    assert s["by_level"] == {"INFO": 2, "ERROR": 1, "WARN": 1}
    assert s["error_rate"] == pytest.approx(0.25)
    assert s["top_paths"] == [("/a", 2), ("/b", 1), ("/c", 1)]


def test_p95_nearest_rank():
    lines = [f"2026-10-26T10:00:{i:02d}Z INFO GET /a 200 {i}ms" for i in range(1, 21)]
    assert summarize(lines)["p95_ms"] == 19


def test_empty_input():
    s = summarize([])
    assert s["total"] == 0 and s["error_rate"] == 0.0 and s["p95_ms"] == 0 and s["top_paths"] == []
