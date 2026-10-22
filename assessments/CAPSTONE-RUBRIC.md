# Capstone assessment rubric

Use this rubric for the ML/legal-information capstone or another substantial project. Score each category 0–4 and link evidence for every score. A high total does not override a critical safety failure.

| Category | 0 — absent | 1 — weak | 2 — partial | 3 — solid | 4 — strong |
|---|---|---|---|---|---|
| Problem and users | No defined user/problem | Assumptions only | Problem stated; limited validation | Clear user need with evidence | Validated need, alternatives considered, scope justified |
| Baseline and data | No source inventory or baseline | Unclear provenance | Sources/baseline partially documented | Credible baseline and source provenance | Reproducible baseline, terms/freshness and data limits documented |
| Correctness and evaluation | No test plan | Demo-only examples | Some tests, weak coverage | Fixed held-out set and measurable criteria | Reproducible evaluation, meaningful comparisons, failure analysis |
| Safety, privacy and security | Critical risks ignored | Controls mostly claims | Some controls implemented | Threats, access, secrets and privacy addressed | Tested controls, negative cases, documented residual risk |
| Reliability and operations | Cannot be run reliably | Manual steps unclear | Repeatable locally with gaps | Documented setup, logs, health checks and cleanup | Failure handling, monitoring, rollback and cost controls demonstrated |
| Engineering quality | Unmaintainable or no tests | Fragile structure | Basic tests and modularity | Readable, tested, reviewed code | Strong tests, clear interfaces, automation and maintainable design |
| Communication | No usable docs | Claims unsupported | Basic README | Reproducible setup, architecture and limitations | Concise demo/write-up with evidence, trade-offs and honest failure report |

## Decision rules

- **Critical fail:** exposed secrets, unauthorised testing, mishandling sensitive user data, misleading financial/legal claims, or evaluation that leaks test data into tuning. Fix these regardless of score.
- **0–12:** not ready for a public demo; narrow the scope and establish a working baseline.
- **13–19:** prototype; state limitations and avoid production claims.
- **20–24:** credible portfolio project if setup and evidence are reproducible.
- **25–28:** strong portfolio candidate; still not equivalent to production approval or independent security review.

A category score of 3 or 4 must cite evidence: a test result, evaluation artifact, design decision, reproducible command, or recorded demo. Do not award points for plans that have not been implemented.

## Project-specific checks for the legal-information capstone

- Answers cite the authoritative source passage; unsupported claims trigger abstention.
- High-stakes, urgent, personal, or out-of-scope situations clearly explain limits and refer to qualified assistance.
- Test set is fixed before tuning; report the plain keyword-search baseline.
- Include prompt-injection attempts, stale/conflicting sources, missing citations, privacy probes, and non-English/accessibility cases where in scope.
- Do not use real sensitive case details in logs or evaluation fixtures.
