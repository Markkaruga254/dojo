"""Source interfaces. Implement one class per verified source (see DATA_SOURCES.md)."""
from __future__ import annotations

from datetime import date
from typing import Protocol

from .models import NewsItem, PriceBar


class PriceSource(Protocol):
    name: str

    def fetch_prices(self, tickers: list[str], day: date) -> list[PriceBar]: ...


class NewsSource(Protocol):
    name: str

    def fetch_news(self) -> list[NewsItem]: ...
