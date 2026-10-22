# Cloud / DevOps track

The depth targets are **deploy, automate, secure, observe**. Build a small service end-to-end instead of collecting disconnected tool tutorials. Prefer one primary cloud (AWS is a sensible default for this plan) and treat other providers as vocabulary until the core workflow is repeatable.

| Week | Topic | Hands-on evidence |
|---|---|---|
| 1 | Linux/CLI + Git | Scripted setup of the dev environment |
| 2 | Docker basics | Build/run/compose the notes API |
| 3 | Containerise a Python service; environment/secrets hygiene | Non-root image, .dockerignore, health check |
| 4 | Managed deployment, if affordable | Deploy a notes API only after checking price, quota, and teardown; otherwise document a local equivalent |
| 5 | CI with GitHub Actions | Test → build; push only when registry credentials and workflow permissions are correctly configured |
| 6 | Terraform basics | Provision a small resource from code; plan and destroy safely |
| 7 | IAM least privilege and secret management | Rotate a secret without placing it in source control |
| 8 | Observability | Structured logs, one useful metric, one alert |
| 9 | Teaching rehearsal | Deliver a 20-minute deploy walkthrough |
| 10 | Managed container platforms and Kubernetes concepts | Explain pod, deployment, service, and ingress |
| 11 | Security overlay | Scan an image if tooling is available; fix and document findings |
| 12–13 | Terraform + CI for the capstone | Repeatable deployment with a documented rollback/cleanup path |
| 14 | System design for a small ML service | Diagram, data flow, failure modes, and trade-offs |
| 15 | Interview review | Answer cloud/DevOps questions aloud |
| 16 | Taper | No new tools; review evidence and weak spots |

## Start here

1. Complete [Lab 01: Linux CLI and Git workflow](labs/lab01_linux_git/README.md). It is local-only and does not require cloud credentials or paid services.
2. Read [Cloud checkpoints](CHECKPOINTS.md) before provisioning or publishing a service.
3. Use [security-overlay.md](security-overlay.md) as a review checklist, not as a substitute for testing.
4. Use [teaching-plan.md](teaching-plan.md) when preparing a reproducible group session.

## Files and workflow

- security-overlay.md: cross-project security checklist.
- CHECKPOINTS.md: milestone evidence, public-deployment gate, and safe cleanup.
- Use your Docker mastery repository as the deeper reference; link to it rather than duplicating the same course.

Cloud services can cost money even when an exercise fails. Check current pricing, set budget alerts where available, use least privilege, and document teardown before creating resources. A local demonstration is acceptable when cloud access or budget is unavailable; mark hosted deployment as deferred rather than claiming it was deployed.
