"""Lab 01: byte-pair encoding on characters (no libraries)."""
from __future__ import annotations


def train_bpe(text: str, num_merges: int) -> list[tuple[str, str]]:
    """Learn merges.

    Start with tokens = list(text). Repeat up to num_merges times:
      count adjacent pairs; pick the most frequent (ties: lexicographically smallest pair);
      stop early if no pair occurs at least twice; merge all non-overlapping occurrences
      left to right into one token (the concatenation); record the pair.
    """
    raise NotImplementedError


def encode(text: str, merges: list[tuple[str, str]]) -> list[str]:
    """Start from characters; apply each merge in the learned order, left to right."""
    raise NotImplementedError


def decode(tokens: list[str]) -> str:
    raise NotImplementedError
