# Lab 01: BPE tokenizer from scratch

## Goal

Implement a small, character-based byte-pair encoding (BPE) learner to understand how frequent adjacent tokens are merged. This is a teaching implementation, not a production tokenizer and not byte-level BPE.

## Build

Implement `train_bpe`, `encode`, and `decode` in `bpe.py`.

- Start training from `list(text)`.
- Count adjacent pairs and choose the most frequent; break ties by lexicographically smallest pair.
- Stop before using a merge if no pair occurs at least twice.
- Merge non-overlapping occurrences from left to right, record each merge, and apply learned merges in order when encoding.
- Decoding concatenates tokens back into the original text.

Do not change the deterministic tie-break rule to make a test pass.

## Verify

Install the optional lab dependencies if needed, then run from this directory:

```bash
python -m pytest -q
```

Before relying on the supplied tests, add checks for at least two of these: empty input, zero merges, repeated pairs, tied pair frequencies, overlapping-looking occurrences, and round-trip `decode(encode(text, merges), ...)` behavior using the merges trained for that text.

## Explain and record

- Why subword tokenisation can handle rare or unseen words better than a word-only vocabulary.
- Why merge ordering and deterministic tie-breaking matter.
- One case where this simplified character-level implementation differs from a production byte-level tokenizer.
- The test command, result, and your added edge cases.

The exercise is intentionally incomplete until the TODOs are implemented. A green test suite is evidence for the tested contract, not proof that this is a complete or production-ready tokenizer.
