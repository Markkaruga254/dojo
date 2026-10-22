# Assessment strategy

Formats for Safaricom and Andela change. **Read your invitation emails and note the platform, duration, languages, allowed libraries and scoring.** Do not assume a format.

## Time management (typical 2-problem, 60–120 min online test)
- 5 min: read both problems, pick the easier first.
- Brute force first and submit it if it passes the samples. Partial credit is real.
- Optimise only after a correct baseline exists.
- Reserve the last 10 min for edge cases and re-reading the statement.

## Constraints → target complexity
| n | Aim for |
|---|---|
| ≤ 10 | O(n!) backtracking |
| ≤ 20 | O(2ⁿ) bitmask / subsets |
| ≤ 500 | O(n³) |
| ≤ 5,000 | O(n²) |
| ≤ 10⁵ | O(n log n) or O(n) |
| ≤ 10⁶+ | O(n) or O(log n) |

## Edge-case checklist
empty input · single element · duplicates · negatives/zero · max size · already sorted/reverse · overflow (rare in Python) · off-by-one on indices.

## Python-specific
`collections` (Counter, defaultdict, deque) · `heapq` · `bisect` · `itertools` · `functools.lru_cache` · slicing cost is O(k) · string concatenation in loops is O(n²) · `sys.setrecursionlimit` for deep DFS (or go iterative) · fast input with `sys.stdin.readline`.

## SQL (often tested alongside)
joins, GROUP BY/HAVING, window functions (ROW_NUMBER, RANK, LAG/LEAD), CTEs, NULL handling.

## Environment dry-run (Week 16)
Same machine, same editor, stable connection + backup data, power, quiet room, allowed tabs. Do one full mock under those conditions.
