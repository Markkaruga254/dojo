# Contributing

Help make Dojo a reliable, practice-first engineering course.

## Learning materials

- Start with the learner outcome, prerequisites, practice task, and verification method. The optional [`docs/LESSON_TEMPLATE.md`](docs/LESSON_TEMPLATE.md) provides a structure when useful.
- Write original explanations and exercises; link to third-party sources instead of copying their content.
- Do not create empty lesson files just to make directories look consistent.
- Keep unfinished starter exercises clearly labelled and separate worked solutions from the first-attempt path where practical.
- For assessments, use the [practical assessment playbook](assessments/PRACTICAL-ASSESSMENT-PLAYBOOK.md) and [capstone rubric](assessments/CAPSTONE-RUBRIC.md).

## Code and tests

- Follow the existing style and add tests for behaviour changes.
- Do not weaken assertions or mark an unrun check as passing.
- Prefer deterministic tests and document any external service, credential, or paid-resource requirement.
- Never commit credentials, tokens, personal data, or generated state files.
- Use authorised environments only for security exercises. Document cleanup and costs for cloud work.

## Pull request checklist

- [ ] The change solves a clear learner problem.
- [ ] Commands and links were checked.
- [ ] Tests were run, or the limitation is stated.
- [ ] Cost, privacy, cleanup, and security considerations are covered where relevant.
- [ ] Curriculum navigation is updated when paths change.
- [ ] Any new completion claim is backed by reproducible evidence.
