import pytest
from retry import retry


def flaky(fail_times, exc=ValueError):
    state = {"calls": 0}

    def fn():
        """doc"""
        state["calls"] += 1
        if state["calls"] <= fail_times:
            raise exc("boom")
        return "ok"
    return fn, state


def test_succeeds_after_failures_with_backoff():
    delays = []
    fn, state = flaky(2)
    wrapped = retry(times=3, base_delay=0.1, sleep=delays.append)(fn)
    assert wrapped() == "ok"
    assert state["calls"] == 3
    assert delays == [0.1, 0.2]


def test_raises_after_exhausting_attempts():
    delays = []
    fn, state = flaky(10)
    wrapped = retry(times=3, base_delay=1, sleep=delays.append)(fn)
    with pytest.raises(ValueError):
        wrapped()
    assert state["calls"] == 3 and delays == [1, 2]


def test_other_exceptions_not_retried():
    delays = []
    fn, state = flaky(5, exc=KeyError)
    wrapped = retry(times=3, exceptions=(ValueError,), sleep=delays.append)(fn)
    with pytest.raises(KeyError):
        wrapped()
    assert state["calls"] == 1 and delays == []


def test_preserves_metadata():
    fn, _ = flaky(0)
    wrapped = retry()(fn)
    assert wrapped.__name__ == "fn" and wrapped.__doc__ == "doc"
