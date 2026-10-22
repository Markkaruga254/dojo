# Course quality audit

This is a working checklist, not a release sign-off. Re-run checks after changes and inspect the CI result before describing a release as verified.

## Strengths

- DSA, applied Python, ML, a product project, cloud/DevOps, assessments, and daily tracking share one repository.
- The dated roadmap includes objective gates.
- The tracker CLI and test-backed labs encourage repeatable practice.
- CI separates core tests from the NSE platform tests.

## Gaps to address

| Area | Observation | Improvement |
|---|---|---|
| Onboarding | Editable install failed because package discovery found multiple top-level directories. | Document direct test-tool installation until package layout is deliberately fixed and tested. |
| ML exercises | Tokenizer and attention starter functions remain intentionally incomplete. | Keep them labelled as exercises; do not claim all labs pass. |
| Hugging Face | Chapter-to-lab mapping is not complete. | Verify it against official current course pages and identify required versus optional work. |
| Evidence | A schedule alone cannot establish mastery. | Use logs, tests, mock retrospectives, project evaluation, and evidence-linked confidence ratings. |
| Project safety | NSE and cloud work involve data, cost, and security risks. | Document data provenance, provider terms, cost controls, cleanup, and credential handling. |
| Verification | Local checks and CI are different environments. | Report exact commands and outcomes; confirm CI before claiming it passed. |

## Local baseline previously reported by the maintainer

- Ruff on scripts, tests, and DSA solutions: passed.
- Core pytest suite: 11 passed.
- NSE platform tests with `PYTHONPATH=nse_platform/src`: 3 passed.
- ML tokenizer and attention starter exercises remain incomplete.
- `pip install -e ".[dev,labs]"` failed due to automatic package discovery across multiple top-level directories.

These are historical local results, not a claim that this GitHub branch has just been tested in a clean environment.

## Release checklist

- [ ] README setup works from a clean checkout.
- [ ] Documented test commands match CI.
- [ ] Local links and curriculum paths resolve.
- [ ] Active modules state prerequisites, tasks, and verification steps.
- [ ] Incomplete exercises are clearly labelled.
- [ ] Hugging Face mappings link to official source material.
- [ ] Capstone and mock rubrics have observable pass criteria.
- [ ] Cost, cleanup, data provenance, and credential handling are documented.
- [ ] Licensing for original and third-party material is clear.
- [ ] CI is green on the release commit.
