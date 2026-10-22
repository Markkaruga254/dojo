import json
import shutil
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import forge

REPO = Path(__file__).resolve().parent.parent


def make_root(tmp_path):
    (tmp_path / "log").mkdir()
    (tmp_path / "config").mkdir()
    shutil.copy(REPO / "log" / "TEMPLATE.md", tmp_path / "log" / "TEMPLATE.md")
    shutil.copy(REPO / "config" / "plan.json", tmp_path / "config" / "plan.json")
    return tmp_path


def test_week_numbers():
    assert forge.week_number(date(2026, 10, 25)) == 0
    assert forge.week_number(date(2026, 10, 26)) == 1
    assert forge.week_number(date(2026, 11, 1)) == 1
    assert forge.week_number(date(2026, 11, 2)) == 2
    assert forge.week_number(date(2027, 2, 14)) == 16


def test_plan_is_complete_and_contiguous():
    weeks = json.loads((REPO / "config" / "plan.json").read_text())["weeks"]
    assert [w["week"] for w in weeks] == list(range(17))
    assert weeks[1]["start"] == "2026-10-26" and weeks[16]["end"] == "2027-02-14"


def test_new_day_fills_template(tmp_path):
    root = make_root(tmp_path)
    path = forge.new_day(date(2026, 10, 27), root)
    text = path.read_text()
    assert "2026-10-27" in text and "Week 1" in text and "{{" not in text
    assert forge.new_day(date(2026, 10, 27), root) == path  # idempotent


def test_add_problem_and_stats(tmp_path):
    root = make_root(tmp_path)
    d = date(2026, 10, 27)
    forge.add_problem(root, d, "Two Sum", "arrays", "easy", "independent", 15, "solved")
    forge.add_problem(root, d, "3Sum", "two-pointers", "medium", "hinted", 40, "solved")
    forge.add_problem(root, d, "Trapping Rain Water", "two-pointers", "hard", "assisted", 50, "failed")
    st = forge.compute_stats(forge.read_tracker(root))
    assert st["attempts"] == 3 and st["solved"] == 2
    assert st["independent_solved"] == 1 and st["independent_rate"] == 0.5
    assert st["by_topic"]["two-pointers"]["attempts"] == 2


def test_invalid_mode_rejected(tmp_path):
    import pytest
    with pytest.raises(ValueError):
        forge.add_problem(make_root(tmp_path), date(2026, 10, 27), "x", "t", "easy", "cheated", 1, "solved")


def test_due_reviews(tmp_path):
    root = make_root(tmp_path)
    forge.add_problem(root, date(2026, 10, 27), "3Sum", "two-pointers", "medium", "hinted", 40, "solved")
    forge.add_problem(root, date(2026, 10, 27), "Two Sum", "arrays", "easy", "independent", 10, "solved")
    rows = forge.read_tracker(root)
    assert forge.due_reviews(rows, date(2026, 10, 29)) == []
    assert forge.due_reviews(rows, date(2026, 10, 31)) == [("3Sum", 4)]


def test_streak(tmp_path):
    root = make_root(tmp_path)
    for day in (25, 26, 27):
        forge.new_day(date(2026, 10, day), root)
    assert forge.streak(root, date(2026, 10, 27)) == 3
    assert forge.streak(root, date(2026, 10, 29)) == 0
