# Course quality audit

This is a working checklist, not a release sign-off. Re-run checks after changes and inspect CI before describing a release as verified.

## Strengths

- DSA, applied Python, ML, a product project, cloud/DevOps, assessments, and daily tracking share one repository.
- The dated roadmap includes objective gates.
- Track-specific checkpoint documents describe observable evidence for DSA, Python, ML, and cloud/DevOps.
- The four current Python lab briefs and two ML lab briefs now give learners explicit build tasks, test commands, edge-case expectations, and evidence/reflection prompts.
- The Hugging Face map links selected official units to the local weekly curriculum and calls out an external unit that was marked as coming soon when checked.
- CI installs the project in editable mode and separates core tests from NSE platform tests.

## Remaining gaps

| Area | Observation | Next improvement |
|---|---|---|
| ML exercises | Tokenizer and attention starter functions remain intentionally incomplete. | Implement them as learner exercises; do not claim all labs pass until the learner completes them and tests pass. |
| Hugging Face | The selected-unit plan is mapped, but the external syllabus can change and the learner still has to record actual completion. | Re-check official navigation before each block and log the exact unit and evidence. |
| Exercise coverage | Current briefs are clearer, but not every track folder uses the same lesson structure, and some curriculum content remains a roadmap/checkpoint rather than a runnable lab. | Audit DSA, cloud, and product-project tasks separately; avoid adding boilerplate where it does not improve learning. |
| Evidence | A schedule alone cannot establish mastery. | Use logs, tests, mock retrospectives, project evaluation, and evidence-linked confidence ratings. |
| Project safety | NSE and cloud work involve data, cost, and security risks. | Document data provenance, provider terms, cost controls, cleanup, and credential handling. |
| Verification | Local checks and CI are different environments. | Report exact commands and outcomes; confirm CI on the latest commit before claiming it passed. |

## Local baseline previously reported by the maintainer

- Ruff on scripts, tests, and DSA solutions: passed.
- Core pytest suite: 11 passed.
- NSE platform tests with PYTHONPATH=nse_platform/src: 3 passed.
- ML tokenizer and attention starter exercises remain intentionally incomplete.
- Historical issue: pip install -e ".[dev,labs]" failed due to automatic package discovery across multiple top-level directories. Explicit package discovery has since been added; CI installs the project in editable mode.

These are historical local results, not a claim that this GitHub branch has just been tested in a clean environment. Check the current commit's CI before release.

## Release checklist

- [ ] README setup works from a clean checkout.
- [ ] Documented test commands match CI.
- [ ] Local links and curriculum paths resolve.
- [ ] Active modules state prerequisites, tasks, and verification steps.
- [ ] Incomplete exercises are clearly labelled.
- [ ] Hugging Face links are checked against current official navigation.
- [ ] Capstone and mock rubrics have observable pass criteria.
- [ ] Cost, cleanup, data provenance, and credential handling are documented.
- [ ] Licensing for original and third-party material is clear.
- [ ] CI is green on the release commit.
