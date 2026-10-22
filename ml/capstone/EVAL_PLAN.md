# Evaluation plan

Fix the test set **before** tuning. Version it. Never train on it.

| Set | Size | Purpose |
|---|---|---|
| Dev | 30–50 questions | iterate |
| Held-out test | 30 questions | report once per milestone |
| Red-team | 20 prompts | injection, out-of-scope, harmful, privacy-leak attempts |

## Metrics
- Retrieval: recall@k (is the right passage in the top k?)
- Answer groundedness: every claim supported by a cited passage (manual check, rubric 0/1)
- Correct refusal/referral rate on out-of-scope or high-stakes questions
- Plain-language readability (manual check by a non-expert)
- Latency and cost per query

## Baselines to beat
1. Keyword search over the same sources.  2. A zero-shot model without retrieval (expected to hallucinate: measure it).

## Report format
Table of metrics (dev, test), 5 worst failures with root cause, what you changed, what you refused to claim.
