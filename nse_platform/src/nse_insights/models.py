"""Core data models and pure helpers (no I/O): easy to test, safe to reuse."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date, datetime
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


@dataclass(frozen=True)
class PriceBar:
    ticker: str
    day: date
    close: float
    volume: int | None = None
    open: float | None = None
    high: float | None = None
    low: float | None = None


@dataclass
class NewsItem:
    url: str
    title: str
    source: str
    published_at: datetime | None = None
    body: str = ""
    tickers: list[str] = field(default_factory=list)


def canonical_url(url: str) -> str:
    """Lowercase scheme/host, drop fragment and utm_* params, strip trailing slash (keep '/')."""
    parts = urlsplit(url.strip())
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
             if not k.lower().startswith("utm_")]
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, urlencode(query), ""))


def dedupe_news(items: list[NewsItem]) -> list[NewsItem]:
    """Keep the first item per canonical URL, preserving order."""
    seen: set[str] = set()
    out: list[NewsItem] = []
    for item in items:
        key = canonical_url(item.url)
        if key not in seen:
            seen.add(key)
            out.append(item)
    return out


def tag_tickers(text: str, universe: dict[str, list[str]]) -> list[str]:
    """Return sorted tickers whose name/alias appears as a whole word/phrase (case-insensitive)."""
    found = set()
    for ticker, aliases in universe.items():
        for alias in aliases:
            if re.search(rf"\b{re.escape(alias)}\b", text, flags=re.IGNORECASE):
                found.add(ticker)
                break
    return sorted(found)
