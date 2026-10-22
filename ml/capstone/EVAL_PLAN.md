# Evaluation plan

Evaluation is a release gate, not a final screenshot. Fix the held-out test set **before** tuning, version it, and keep it out of prompt, retrieval, threshold, and model selection work. Store synthetic or redacted examples in the repository; never commit real sensitive legal cases.

## Evaluation sets

| Set | Suggested size | Purpose | May guide changes? |
|---|---:|---|---|
| Development | 30–50 questions | Iterate on retrieval, wording, and UX | Yes |
| Held-out test | 30 questions | Compare approaches at named milestones | No; inspect only for reporting after the approach is frozen |
| Red-team | 20 prompts | Injection, out-of-scope, harmful requests, stale/conflicting sources, privacy-leak attempts | Use a separate version for iterative fixes; reserve unseen cases for final checks |

These sizes are starting targets, not a reason to invent or pad questions. If the available dataset is smaller, report the actual size and its limitations.

## Record for every case

Use a stable case ID and record:
- question, expected source or expected refusal/referral, and risk category;
- retrieved passage IDs and whether the expected source appeared in the top *k*;
- whether every material answer claim is supported by a cited passage;
- correct answer, appropriate abstention, or referral outcome;
- latency and estimated cost, where measurable;
- reviewer notes and failure category.

Keep source text/licensing and collection dates in the source inventory. Do not include names, case numbers, contact details, or other real personal case data in fixtures.

## Metrics

- **Retrieval recall@k:** relevant source passage present in the top *k*, divided by cases with a known relevant passage.
- **Citation support:** proportion of reviewed material claims supported by the cited passage; report unsupported claims separately.
- **Correct abstention/referral:** proportion of out-of-scope, unanswerable, urgent, or high-stakes cases that correctly abstain or refer.
- **Answer usefulness and readability:** manual rubric with examples; ideally have a non-expert review plain-language quality.
- **Operational:** latency and cost per query, plus failures/timeouts.

Always report denominators and the scoring rule. A percentage without the number of cases reviewed is not enough. Do not combine safety-critical failures into an average score that hides them.

## Baselines to compare

1. Keyword search over the same source collection.
2. If appropriate and safe, a zero-shot model without retrieval as a diagnostic comparison—not as an assumed production candidate.
3. The selected approach, evaluated on the same cases and with the same scoring rules.

## Minimum report format

| Version/date | Approach | Dataset version and n | Retrieval recall@k | Citation support | Correct abstention/referral | Latency/cost | Critical failures |
|---|---|---:|---:|---:|---:|---|---|

Also publish:
- the five worst failures with root cause and remediation;
- a short comparison against the keyword baseline;
- limitations, missing evidence, and what you refused to claim;
- exact command/configuration needed to reproduce the run, without credentials.

## Release gate

Do not release a public demo if a critical safety/privacy failure remains, citations are fabricated, or high-stakes questions receive confident unsupported guidance. Fix the issue and rerun affected tests plus the held-out release evaluation. Keep the original report so the improvement is auditable; do not silently replace failed results.
