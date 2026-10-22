# DSA track

Goal: go from "never opened LeetCode" to solving unseen medium problems in ~30 min, in Python, by Week 12, and to do it under test conditions by Week 16.

## Method (per problem)
1. Read, restate, write 2 examples + 1 edge case.
2. Brute force first. State its complexity.
3. Name the pattern (`PATTERNS.md`). Optimise.
4. Code, run your own tests, then the platform's.
5. Record it: `python scripts/forge.py problem "<name>" --topic <t> --difficulty <d> --mode <independent|hinted|assisted> --minutes <m> --result <solved|partial|failed>`
6. If not independent: write the *insight* in one sentence in your log and schedule the re-solve (3 / 7 / 21 days).

## Files
- `CURRICULUM.md`: week-by-week topics and quotas
- `PROBLEMS.md`: curated list (~150), grouped by topic with difficulty
- `PATTERNS.md`: Python templates for each core pattern (read, then re-write from memory)
- `templates/solution_template.py`: how to store a solution
- `solutions/`: your solutions (one folder per topic); a worked example is included
- `tracker.csv`: written by `forge problem`

## Rules
- Do not memorise solutions: memorise patterns and the *reason* each works.
- Easy problems: ≤ 20 min. Medium: ≤ 40. Hard: exposure only until Week 9.
- Never grind past 90 minutes on one problem; hint, learn, re-solve cold later.
