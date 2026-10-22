# Cloud / DevOps track

The depth targets are **deploy, automate, secure, observe**. Build a small service end-to-end instead of collecting disconnected tool tutorials. Prefer one primary cloud (AWS is a sensible default for this plan) and treat other providers as vocabulary until the core workflow is repeatable.

## Lab sequence

| Order | Lab | Outcome | Cost |
|---|---|---|---|
| 1 | [Linux CLI and Git](labs/lab01_linux_git/README.md) | Inspect a local environment, make a safe local commit, and verify a loopback-only service | Free/local |
| 2 | [Dockerise the Notes API](labs/lab02_docker_notes_api/README.md) | Build and inspect a non-root container, verify health and API behavior, clean up | Free/local; Docker required |
| 3 | [CI for a pull request](labs/lab03_ci_pull_request/README.md) | Prove that lint/tests run, catch a deliberate failure, review workflow permissions | Free tier may have limits |
| 4 | [Terraform local resource](labs/lab04_terraform_local/README.md) | Practise plan/apply/destroy and state hygiene without cloud resources | Free/local |

Complete the local labs before provisioning cloud resources. Each lab requires evidence of what actually ran; reading the instructions is not completion.

## Free supporting resources

Use the [free-first resource guide](../docs/RESOURCE_GUIDE.md#cloud-and-devops) to pair each local lab with official Linux/Git, Docker, GitHub Actions, and Terraform material. Read only what you need for the current lab, then produce the evidence listed here. Local labs come before any billable cloud work.

## Suggested 16-week progression

| Week | Topic | Hands-on evidence |
|---|---|---|
| 1 | Linux/CLI + Git | Complete Lab 01 and explain the observations |
| 2 | Docker basics | Complete Lab 02 against the completed Notes API |
| 3 | Container hardening | Non-root image, minimal build context, health check, image review |
| 4 | Managed deployment, if affordable | Deploy only after checking current pricing, quota, and teardown; otherwise document a local equivalent |
| 5 | CI with GitHub Actions | Complete Lab 03 and link a real passing workflow run |
| 6 | Infrastructure as code | Complete Lab 04 locally, then study a cloud resource plan without applying it until reviewed |
| 7 | IAM least privilege and secret management | Rotate a test secret without putting it in source control |
| 8 | Observability | Structured logs, one useful metric, one alert |
| 9 | Teaching rehearsal | Deliver a 20-minute deploy walkthrough |
| 10 | Managed container platforms and Kubernetes concepts | Explain pod, deployment, service, and ingress |
| 11 | Security overlay | Scan an image if tooling is available; fix and document findings |
| 12–13 | Terraform + CI for a capstone | Repeatable deployment with a documented rollback/cleanup path |
| 14 | System design for a small ML service | Diagram, data flow, failure modes, and trade-offs |
| 15 | Interview review | Answer cloud/DevOps questions aloud |
| 16 | Taper | Review evidence and weak spots; avoid starting new tools |

## Start here

1. Complete [Cloud checkpoints](CHECKPOINTS.md) and read the [security overlay](security-overlay.md).
2. Complete the four local labs above in order, keeping notes and evidence.
3. Use [teaching-plan.md](teaching-plan.md) when preparing a reproducible group session.
4. Use the Docker mastery repository as a deeper reference where relevant; link to it rather than duplicating a second course.

Cloud services can cost money even when an exercise fails. Check current pricing, set budget alerts where available, use least privilege, and document teardown before creating resources. A local demonstration is acceptable when cloud access or budget is unavailable; mark hosted deployment as deferred rather than claiming it was deployed.
