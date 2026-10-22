# Course quality audit

This is a working checklist, not a release sign-off. Re-run checks after changes and inspect CI before describing a release as verified.

## Strengths

- DSA, applied Python, ML, a product project, cloud/DevOps, assessments, and daily tracking share one repository.
- The dated roadmap includes objective gates.
- Track-specific checkpoint documents describe observable evidence for DSA, Python, ML, and cloud/DevOps.
- The four current Python lab briefs and two ML lab briefs give learners explicit build tasks, test commands, edge-case expectations, and evidence/reflection prompts.
- The Hugging Face map links selected official units to the local weekly curriculum and flags an external unit that was marked as coming soon when checked.
- CI installs the project in editable mode and separates core tests from NSE platform tests.
- The legal-information capstone now separates problem validation, source inventory, baseline, local prototype, evaluation, and release decisions; deployment is not treated as proof of quality.

## Remaining gaps

| Area | Observation | Next improvement |
|---|---|---|
| ML exercises | Tokenizer and attention starter functions remain intentionally incomplete. | Keep them labelled as learner exercises; do not claim all labs pass until the learner completes them and tests pass. |
| Hugging Face | The selected-unit plan is mapped, but the external syllabus can change and the learner still has to record actual completion. | Re-check official navigation before each block and log the exact unit and evidence. |
| DSA practice | The problem list, pattern notes, and checkpoints provide a study loop, but most listed problems are external platform tasks rather than locally executable exercises. | Keep attempt status honest; add local tests only where they improve feedback, and verify unseen transfer through timed mocks. |
| Cloud/DevOps | The track has milestone evidence and a security/cost gate, but it is a roadmap, not a complete set of runnable labs. | Build one small, low-cost lab at a time with a verified local fallback, cleanup steps, and evidence before expanding the toolset. |
| Capstone evaluation | The evaluation plan defines datasets and metrics, but no result is valid until a real, versioned run is recorded. | Record actual dataset versions, denominators, failures, command/configuration, and cost; never fill tables with target or fabricated values. |
| Evidence | A schedule, badge, or planned activity cannot establish mastery. | Use logs, tests, mock retrospectives, project evaluation, and evidence-linked confidence ratings. |
| Project safety | NSE and cloud work involve data, cost, and security risks. | Verify data provenance and provider terms; use cost controls, cleanup, least privilege, and credential hygiene. |
| Verification | Local checks and CI are different environments. | Report exact commands and outcomes; confirm CI on the latest commit before claiming it passed. |

## Historical local baseline

Previously reported maintainer results:

- Ruff on scripts, tests, and DSA solutions: passed.
- Core pytest suite: 11 passed.
- NSE platform tests with PYTHONPATH=nse_platform/src: 3 passed.
- ML tokenizer and attention starter exercises remain intentionally incomplete.
- Historical issue: pip install -e ".[dev,labs]" failed due to automatic package discovery across multiple top-level directories. Explicit package discovery has since been added; CI installs the project in editable mode.

These are historical results, not a claim that the current branch has just been tested in a clean environment. The current commit's CI is the source of truth for automated verification.

## Release checklist

- [ ] README setup works from a clean checkout.
- [ ] Documented test commands match CI.
- [ ] Local links and curriculum paths resolve.
- [ ] Active labs state prerequisites, tasks, and verification steps.
- [ ] Incomplete exercises are clearly labelled.
- [ ] Hugging Face links are checked against current official navigation.
- [ ] Capstone and mock rubrics have observable pass criteria.
- [ ] Cost, cleanup, data provenance, privacy, and credential handling are documented.
- [ ] Licensing for original and third-party material is clear.
- [ ] CI is green on the exact release commit.
