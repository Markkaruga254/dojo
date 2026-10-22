#!/usr/bin/env python3
"""forge: tiny CLI for the Forge-90 daily practice system.

Commands
  new-day [--date YYYY-MM-DD]   create the day's log from the template
  problem NAME --topic T ...    record a DSA attempt in dsa/tracker.csv
  stats                         DSA + consistency statistics
  week [--date YYYY-MM-DD]      show the week's plan
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START = date(2026, 10, 26)  # Monday of Week 1
FIELDS = ["date", "problem", "topic", "difficulty", "mode", "minutes", "result", "notes"]
MODES = ("independent", "hinted", "assisted")
RESULTS = ("solved", "partial", "failed")
DIFFICULTIES = ("easy", "medium", "hard")
REVIEW_GAPS = (3, 7, 21)


def week_number(d: date) -> int:
    """Week 0 = setup days before START; Week 1 starts on START."""
    if d < START:
        return 0
    return (d - START).days // 7 + 1


def load_plan(root: Path = ROOT) -> list[dict]:
    with open(root / "config" / "plan.json", encoding="utf-8") as fh:
        return json.load(fh)["weeks"]


def plan_for(d: date, root: Path = ROOT) -> dict | None:
    n = week_number(d)
    return next((w for w in load_plan(root) if w["week"] == n), None)


def log_path(d: date, root: Path = ROOT) -> Path:
    return root / "log" / f"{d:%Y}" / f"{d:%m}" / f"{d.isoformat()}.md"


def new_day(d: date, root: Path = ROOT) -> Path:
    path = log_path(d, root)
    if path.exists():
        return path
    text = (root / "log" / "TEMPLATE.md").read_text(encoding="utf-8")
    plan = plan_for(d, root) or {}
    fills = {
        "{{DATE}}": d.isoformat(),
        "{{WEEKDAY}}": d.strftime("%A"),
        "{{WEEK}}": str(week_number(d)),
        "{{PHASE}}": plan.get("phase", "-"),
        "{{DSA}}": plan.get("dsa", "-"),
        "{{PYTHON}}": plan.get("python", "-"),
        "{{ML}}": plan.get("ml", "-"),
        "{{PLATFORM}}": plan.get("platform", "-"),
    }
    for key, value in fills.items():
        text = text.replace(key, value)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def tracker_path(root: Path = ROOT) -> Path:
    return root / "dsa" / "tracker.csv"


def add_problem(root: Path, d: date, problem: str, topic: str, difficulty: str,
                mode: str, minutes: int, result: str, notes: str = "") -> None:
    if mode not in MODES:
        raise ValueError(f"mode must be one of {MODES}")
    if result not in RESULTS:
        raise ValueError(f"result must be one of {RESULTS}")
    if difficulty not in DIFFICULTIES:
        raise ValueError(f"difficulty must be one of {DIFFICULTIES}")
    path = tracker_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not path.exists() or path.stat().st_size == 0
    with open(path, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow({"date": d.isoformat(), "problem": problem, "topic": topic,
                         "difficulty": difficulty, "mode": mode, "minutes": minutes,
                         "result": result, "notes": notes})


def read_tracker(root: Path = ROOT) -> list[dict]:
    path = tracker_path(root)
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def compute_stats(rows: list[dict]) -> dict:
    solved = [r for r in rows if r["result"] == "solved"]
    independent = [r for r in solved if r["mode"] == "independent"]
    by_topic: dict[str, dict[str, int]] = {}
    for r in rows:
        t = by_topic.setdefault(r["topic"], {"attempts": 0, "independent_solved": 0})
        t["attempts"] += 1
        if r["result"] == "solved" and r["mode"] == "independent":
            t["independent_solved"] += 1
    minutes = [int(r["minutes"]) for r in rows if str(r["minutes"]).isdigit()]
    return {
        "attempts": len(rows),
        "solved": len(solved),
        "independent_solved": len(independent),
        "independent_rate": (len(independent) / len(solved)) if solved else 0.0,
        "by_mode": dict(Counter(r["mode"] for r in rows)),
        "by_topic": by_topic,
        "avg_minutes": (sum(minutes) / len(minutes)) if minutes else 0.0,
    }


def due_reviews(rows: list[dict], today: date) -> list[tuple[str, int]]:
    """Problems that were not solved independently and hit a 3/7/21-day mark today or earlier (not yet re-solved)."""
    out = []
    last: dict[str, dict] = {}
    for r in rows:
        last[r["problem"]] = r  # latest attempt wins
    for name, r in last.items():
        if r["mode"] == "independent" and r["result"] == "solved":
            continue
        age = (today - date.fromisoformat(r["date"])).days
        gap = next((g for g in REVIEW_GAPS if age >= g), None)
        if gap is not None and age >= REVIEW_GAPS[0]:
            out.append((name, age))
    return sorted(out, key=lambda x: -x[1])


def streak(root: Path, today: date) -> int:
    d = today if log_path(today, root).exists() else today - timedelta(days=1)
    n = 0
    while log_path(d, root).exists():
        n += 1
        d -= timedelta(days=1)
    return n


def _date(arg: str | None) -> date:
    return datetime.strptime(arg, "%Y-%m-%d").date() if arg else date.today()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="forge", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("new-day"); s.add_argument("--date")
    s = sub.add_parser("week"); s.add_argument("--date")
    sub.add_parser("stats")
    s = sub.add_parser("problem")
    s.add_argument("name"); s.add_argument("--topic", required=True)
    s.add_argument("--difficulty", required=True, choices=DIFFICULTIES)
    s.add_argument("--mode", required=True, choices=MODES)
    s.add_argument("--minutes", type=int, required=True)
    s.add_argument("--result", required=True, choices=RESULTS)
    s.add_argument("--notes", default=""); s.add_argument("--date")

    a = p.parse_args(argv)
    if a.cmd == "new-day":
        print(new_day(_date(a.date)))
    elif a.cmd == "week":
        d = _date(a.date)
        w = plan_for(d)
        if not w:
            print("No plan for this date (outside the 16 weeks).")
            return 1
        print(f"Week {w['week']} ({w['start']} to {w['end']}): {w['phase']}: {w['theme']}")
        for k in ("dsa", "python", "ml", "platform", "cloud", "gate"):
            print(f"  {k:9}{w[k]}")
    elif a.cmd == "problem":
        add_problem(ROOT, _date(a.date), a.name, a.topic, a.difficulty, a.mode,
                    a.minutes, a.result, a.notes)
        print("recorded")
    elif a.cmd == "stats":
        rows = read_tracker()
        st = compute_stats(rows)
        today = date.today()
        print(f"Attempts {st['attempts']} | solved {st['solved']} | independent {st['independent_solved']} "
              f"({st['independent_rate']:.0%} of solved) | avg {st['avg_minutes']:.0f} min")
        print("Modes:", st["by_mode"])
        for t, v in sorted(st["by_topic"].items()):
            print(f"  {t:18} attempts {v['attempts']:3}  independent solved {v['independent_solved']:3}")
        print("Log streak (days):", streak(ROOT, today))
        due = due_reviews(rows, today)
        if due:
            print("Re-solve due:", ", ".join(f"{n} ({age}d)" for n, age in due[:10]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
