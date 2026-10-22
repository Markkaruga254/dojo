"""Lab 04: price parsing and simple analytics."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Bar:
    ticker: str
    day: date
    close: float
    volume: int


def parse_prices(csv_text: str) -> list[Bar]:
    """Parse CSV text with header `ticker,date,close,volume`.

    Skip rows with a missing/non-numeric close or volume, an invalid date, or a close <= 0.
    Return bars sorted by (ticker, day).
    """
    raise NotImplementedError


def daily_returns(bars: list[Bar]) -> dict[str, list[tuple[date, float]]]:
    """Per ticker (bars already sorted): list of (day, close / previous_close - 1); first bar omitted."""
    raise NotImplementedError


def max_drawdown(closes: list[float]) -> float:
    """Largest peak-to-trough fall as a positive fraction of the peak (0.0 if never falls)."""
    raise NotImplementedError
