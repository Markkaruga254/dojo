# Cloud and DevOps checkpoints

The goal is to demonstrate **deploy, automate, secure, observe** with a small service. Do not provision resources merely to collect screenshots; every cloud exercise needs a cost estimate and cleanup plan.

## Local foundation gates

| Gate | Required evidence | Pass condition |
|---|---|---|
| Linux and Git | Commands and sanitised notes from [Lab 01](labs/lab01_linux_git/README.md) | Explain process, disk, memory, ports, staged diff, and secret exclusion |
| Container basics | [Lab 02](labs/lab02_docker_notes_api/README.md), Dockerfile and .dockerignore review | API tests pass; image builds; health endpoint responds; non-root and loopback checks pass |
| CI/CD | [Lab 03](labs/lab03_ci_pull_request/README.md), workflow run URL and commit SHA | A real test failure is detected, fixed, and followed by a passing run |
| Infrastructure as code | [Lab 04](labs/lab04_terraform_local/README.md), sanitised plan and teardown notes | Only the intended local file is managed; state/plan artifacts are excluded |
| Container hardening | Config review and scan result if a scanner is available | No known secret leakage; risks and scanner limitations recorded |

## Milestones

| Milestone | Demonstration | Evidence |
|---|---|---|
| Managed deployment | Deploy one small service only after checking current prices and free-tier limits | Test endpoint, deployment instructions, cost and rollback notes |
| IAM and secrets | Demonstrate least privilege and rotate a secret without placing it in source control | Policy review and documented rotation steps |
| Observability | Emit structured logs, define one meaningful health metric, and troubleshoot an induced failure | Sample logs, alert condition, incident note |
| Capstone operations | Explain how to configure, update, roll back, and safely shut down the service | Runbook and evidence linked from project README |

## Security gate

Before any public deployment, verify:

- [ ] No secrets, tokens, personal data, state files, or plan files are committed.
- [ ] Authentication and authorisation are explicit; routes are not public by accident.
- [ ] Input validation, rate limits, and useful error responses are in place.
- [ ] Logs do not leak credentials, private prompts, or sensitive user data.
- [ ] IAM follows least privilege and cloud credentials are short-lived where possible.
- [ ] Cost limits/alerts are configured where supported and teardown is documented.
- [ ] Security testing is limited to systems you own or have permission to test.
- [ ] Rollback, data retention, and service shutdown have been practised.

Use [security-overlay.md](security-overlay.md) as the project-wide checklist. A local Docker demonstration is acceptable when cloud budget or account access is unavailable; mark cloud deployment as deferred rather than claiming it was deployed.

## Final evidence bundle

Link a repository or sanitized evidence directory containing:
- commands and tool versions;
- the exact commit SHA and passing CI run;
- Dockerfile/.dockerignore and health/API test results;
- Terraform plan/apply/destroy notes for the local exercise;
- security findings, mitigations, and known limitations;
- cost assumptions and cleanup evidence for any cloud resource.

Screenshots alone are not sufficient evidence, and a green CI run only validates the checks that actually ran.
