# Lab 03: Continuous integration for a pull request

## Outcome

Make a small Python service prove its quality automatically on every pull request. The objective is a reproducible test gate, not a green badge without meaningful tests.

## Prerequisites

- Git and a GitHub repository you own or are authorised to change.
- A working local test command for the Notes API or another small Python project.
- Read the existing repository workflow at .github/workflows/ci.yml before writing a second workflow.

This repository already has a core CI workflow. Use it as a reference; do not create a duplicate workflow in the course repository just to complete this lab. Practise in a fork, a dedicated branch, or a small separate repository.

## Task 1 — Define the gate

Write down the exact commands that must pass locally before review. At minimum, use linting for completed Python modules and the relevant automated tests. Do not include intentionally incomplete learner starter files in a lint gate unless the task is to complete them.

Your workflow should:

- trigger on pull_request and push to the default branch;
- use a supported, explicit Python version;
- grant only contents: read unless a documented step needs more;
- install dependencies from the project manifest;
- run lint and tests as separate steps;
- fail on a non-zero command exit;
- avoid secrets, deployment, publishing, or cloud credentials.

Use the current workflow as a style reference and verify action versions against the official GitHub Actions documentation when editing a real workflow.

## Task 2 — Test the workflow with a deliberate failure

Create a branch and make a small test-backed change. Open a pull request and confirm the expected workflow runs on that exact commit. Then, in a temporary follow-up commit, introduce a known failing assertion. Confirm CI turns red for the expected reason, revert the deliberate failure, and confirm the repaired run is green.

Do not merge the intentionally failing commit. Do not disable a check to make the badge green.

## Task 3 — Review permissions and supply chain

Inspect workflow permissions and every action reference. Prefer least privilege and pin third-party actions to verified full commit SHAs when the repository's maintenance policy supports that workflow. Do not copy a SHA from an untrusted blog or assume a tag is immutable. Avoid pull-request workflows that execute untrusted fork code with write permissions or expose repository secrets.

Do not add deployment to this lab. Build/test automation is the gate; CD requires a separate review of environment protection, credentials, rollback, and cost.

## Evidence and exit criteria

- [ ] The workflow triggers on pull requests and default-branch pushes.
- [ ] The test and lint commands match documented local commands.
- [ ] A real successful run is linked to the final commit.
- [ ] A deliberate test failure was detected and then reverted.
- [ ] Workflow permissions and secret exposure were reviewed.
- [ ] The final branch has no deliberate failing test.

Record the commit SHA, workflow run URL, failure cause, repair, and remaining gaps. A green workflow only proves the checks configured in that workflow ran successfully.
