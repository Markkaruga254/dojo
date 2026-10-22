# Cloud / DevOps track

Light-touch but real: you teach deployment on the GDG Cloud Track and the capstone and platform need it. The depth targets are *deploy, automate, secure, observe*.

| Wk | Topic | Hands-on |
|---|---|---|
| 1 | Linux/CLI + Git | scripted setup of your dev box |
| 2 | Docker basics | build/run/compose the notes API |
| 3 | Containerise a Python service, env/secrets hygiene | non-root image, `.dockerignore`, healthcheck |
| 4 | Deploy a container to a managed service (Cloud Run / ECS / similar) | public URL for the notes API |
| 5 | CI with GitHub Actions | test → build → push |
| 6 | Terraform basics | provision a bucket + service from code |
| 7 | IAM least privilege, secrets managers | rotate a secret without redeploying |
| 8 | Observability | structured logs, a metric, one alert |
| 9 | Teaching rehearsal | deliver a 20-min deploy walkthrough |
| 10 | Managed container platforms, Kubernetes concepts (read-level) | explain pod/deployment/service/ingress |
| 11 | Security overlay (`security-overlay.md`) | scan an image, fix findings |
| 12–13 | Terraform + CI for the capstone | one-command deploy |
| 14 | System design for a small ML service | whiteboard it |
| 15 | Interview review (`assessments/interview/devops_cloud.md`) | answer aloud |
| 16 | Rest | none |

Existing repos: keep your Docker mastery repo as the deep reference; link it, do not copy it here. Pick one primary cloud to be fluent in (AWS first is a sensible default) and treat the others as vocabulary.
