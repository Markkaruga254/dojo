# DSA track

Goal: go from "never opened LeetCode" to solving unseen medium problems in about 30 minutes, in Python, by Week 12, and to do it under test conditions by Week 16. This is a target to test, not a guarantee.

## Method (per problem)

1. Read, restate, write two examples and one edge case.
2. Brute force first. State its complexity.
3. Name the pattern in PATTERNS.md. Optimise.
4. Code, run your own tests, then the platform's.
5. Record it with the tracker command below.
6. If not independent: write the insight in one sentence in your log and schedule the re-solve (3 / 7 / 21 days).

```bash
python scripts/forge.py problem "<name>" --topic <t> --difficulty <d> --mode <independent|hinted|assisted> --minutes <m> --result <solved|partial|failed>
```

## Files

- CURRICULUM.md: week-by-week topics and quotas
- PROBLEMS.md: curated list, grouped by topic and difficulty
- PATTERNS.md: Python templates for core patterns; read, then rewrite from memory
- CHECKPOINTS.md: per-topic exit criteria, roadmap gates, and mock protocol
- templates/solution_template.py: how to store a solution
- solutions/: your solutions; a worked example is included
- tracker.csv: written by the tracker

## Free supporting resources

Use the [free-first resource guide](../docs/RESOURCE_GUIDE.md#dsa-and-interview-problem-solving) when a pattern is unclear. Prefer [VisuAlgo](https://visualgo.net/en) for visual intuition and [CP-Algorithms](https://cp-algorithms.com/) for deeper reading; then close the tabs and solve the current problem independently. The local problem list and checkpoints still decide what to practise.

## Rules

- Do not memorise solutions: learn patterns and why they work.
- Easy problems: aim for 20 minutes or less. Medium: aim for 40 minutes or less. Hard: exposure only until Week 9.
- Never grind past 90 minutes on one problem; ask for a hint, learn, then re-solve cold later.
- Mark hinted or assisted attempts honestly. A copied or hinted solution is not an independent solve.

Start with [DSA checkpoints](CHECKPOINTS.md) to understand what evidence is required at each gate.
