# Security overlay (applies to every project)
- **Secrets:** never in git; `.env` ignored; use a secret manager in cloud; scan history with a secret scanner before pushing.
- **Containers:** minimal base image, non-root user, pinned versions, no build tools in the final image, image scan in CI.
- **CI/CD:** least-privilege tokens, OIDC to cloud instead of long-lived keys, pinned action versions, protected main branch.
- **IAM:** start from deny; one role per service; no wildcard actions/resources; review with an access analyzer.
- **APIs:** authn + authz on every route, input validation, rate limiting, CORS locked down, security headers, no stack traces to clients.
- **ML workloads:** treat prompts and retrieved text as untrusted input (prompt injection); no secrets in prompts; log redaction; pin model versions; rate-limit and cap cost.
- **Data:** minimise collection; encrypt in transit and at rest; define retention.
Checklist habit: run it against each deployed service in Weeks 11–13 and record findings in your log.
