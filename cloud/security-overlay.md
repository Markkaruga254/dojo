# Security overlay (applies to every project)

Use this as a review aid, not as proof that a system is secure. Record findings and unresolved risks rather than ticking boxes without evidence.

- **Secrets:** never commit credentials; ignore real .env files; use a secret manager in cloud; scan the intended diff and history before publishing.
- **Containers:** use a supported minimal base image, non-root user, narrow build context, pinned runtime dependencies, no build tools in the final image when avoidable, and image scanning where available.
- **CI/CD:** grant least-privilege workflow permissions; avoid exposing secrets to untrusted pull-request code; verify third-party actions; use OIDC rather than long-lived cloud keys where supported; protect deployment environments.
- **IAM:** start from deny; one role per service; scope actions and resources narrowly; review policies with an access analyser.
- **APIs:** authentication and authorisation on every protected route, input validation, rate limiting appropriate to the service, restrictive CORS, useful errors, and no stack traces or secrets in client responses.
- **ML workloads:** treat prompts and retrieved text as untrusted input; do not put secrets in prompts; minimise/redact logs; pin model and dataset versions; rate-limit and cap cost.
- **Data:** minimise collection; document source, licence/terms, freshness, retention, and deletion; protect data in transit and at rest when applicable.
- **Cloud cost:** estimate costs before provisioning, set budgets/alerts where supported, tag resources, document owner and teardown command, and verify resources were removed after the exercise.
- **Supply chain:** pin and review dependencies where practical; inspect scanner results and understand what they do not cover.

Before a public deployment, review the checklist in [Cloud checkpoints](CHECKPOINTS.md) and record evidence for each applicable control. Only test systems you own or have permission to assess.
