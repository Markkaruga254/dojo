# Cloud and DevOps checkpoints

The goal is to demonstrate **deploy, automate, secure, observe** with a small service. Do not provision resources merely to collect screenshots; every cloud exercise needs a cost estimate and cleanup plan.

## Milestones

| Milestone | Demonstration | Evidence |
|---|---|---|
| Linux and Git | Diagnose a process, inspect ports, use environment variables safely, and explain a shell pipeline | Reproducible commands and notes |
| Container basics | Build and run a service with a health check; explain image vs container | Dockerfile, successful local run, health-check output |
| Secure container | Run as non-root, use a .dockerignore, avoid embedding secrets, and keep the image minimal | Config review and scan result if a scanner is available |
| CI/CD | Run lint/tests automatically on a pull request with read-only default permissions | Workflow file and actual passing workflow run |
| Infrastructure as code | Provision one small resource using variables and outputs; explain plan/apply/destroy | Sanitised plan, state excluded from Git, destroy confirmation |
| IAM and secrets | Demonstrate least privilege and rotate a secret without placing it in source control | Policy review and documented rotation steps |
| Observability | Emit structured logs, define one meaningful health metric, and troubleshoot an induced failure | Sample logs, alert condition, incident note |
| Deployment | Deploy one small service only after checking current prices and free-tier limits | Test endpoint, deployment instructions, cost and rollback notes |
| Capstone operations | Explain how to configure, update, roll back, and safely shut down the service | Runbook and evidence linked from the project README |

## Security gate

Before any public deployment, verify:

- [ ] No secrets, tokens, personal data, or state files are committed.
- [ ] Authentication and authorisation are explicit; routes are not public by accident.
- [ ] Input validation, rate limits, and useful error responses are in place.
- [ ] Logs do not leak credentials, private prompts, or sensitive user data.
- [ ] IAM follows least privilege and cloud credentials are short-lived where possible.
- [ ] Cost limits/alerts are configured where supported and teardown is documented.
- [ ] Security testing is limited to systems you own or have permission to test.

Use the security overlay in security-overlay.md as the project-wide checklist. A local Docker demonstration is acceptable when cloud budget or account access is unavailable; mark cloud deployment as deferred rather than claiming it was deployed.
