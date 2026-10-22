"""Two Sum (easy, arrays/hashing): worked example.
Pattern: hash map complement lookup.
Brute force: all pairs, O(n^2) time, O(1) space.
Optimal: one pass storing value -> index, O(n) time, O(n) space.
Insight: for each x, I only need to know whether (target - x) appeared earlier.
"""
from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
