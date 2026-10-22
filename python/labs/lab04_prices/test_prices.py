from datetime import date

import pytest
from prices import Bar, daily_returns, max_drawdown, parse_prices

CSV = """ticker,date,close,volume
SCOM,2026-10-02,30.0,1000
SCOM,2026-10-01,29.0,900
KCB,2026-10-01,80.0,500
KCB,2026-10-02,,500
SCOM,2026-10-03,abc,100
SCOM,not-a-date,31.0,100
SCOM,2026-10-04,31.0,xyz
SCOM,2026-10-05,-1,10
"""


def test_parse_skips_bad_rows_and_sorts():
    bars = parse_prices(CSV)
    assert bars == [
        Bar("KCB", date(2026, 10, 1), 80.0, 500),
        Bar("SCOM", date(2026, 10, 1), 29.0, 900),
        Bar("SCOM", date(2026, 10, 2), 30.0, 1000),
    ]


def test_daily_returns():
    bars = parse_prices(CSV)
    out = daily_returns(bars)
    assert out["KCB"] == []
    assert out["SCOM"][0][0] == date(2026, 10, 2)
    assert out["SCOM"][0][1] == pytest.approx(30.0 / 29.0 - 1)


def test_max_drawdown():
    assert max_drawdown([100, 120, 90, 110, 80]) == pytest.approx(40 / 120)
    assert max_drawdown([1, 2, 3]) == 0.0
    assert max_drawdown([]) == 0.0
