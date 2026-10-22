# Lab 02: Containerise the Notes API

## Outcome

Package the completed Python Notes API as a reproducible container, run it as a non-root user, and verify its HTTP behavior from the host. This lab is local-first: do not publish an image or expose the service to the public internet.

## Prerequisites

- Complete the required endpoints in python/labs/lab03_notes_api/README.md and pass that lab's tests.
- Docker Engine or Docker Desktop running.
- Repository optional dependencies installed with pip install -e ".[labs]".

From the repository root, run the Notes API tests first. If they fail, fix the API before debugging Docker.

## Task 1 — Add a health endpoint and test it

Add GET /health to the Notes API. It should return a small JSON object such as {"status": "ok"} and status 200. Add a test that verifies both the status code and response body. Keep the endpoint free of sensitive configuration details; it must not return environment variables, filesystem paths, or credentials.

Run the Notes API tests and record the exact result. The in-memory store is acceptable for this exercise; explain that data disappears when the container stops.

## Task 2 — Create a safe build context

Create a Dockerfile beside the Notes API source, or create a small dedicated service directory containing only the completed app and its requirements. Use a small supported Python base image, install only runtime dependencies, copy only the files needed to run the service, and configure the process to listen on 0.0.0.0 inside the container.

The final image must run as a non-root user. Do not copy .env files, Git metadata, tests, virtual environments, caches, local data, or credentials into the image. Add and inspect a .dockerignore. Pin the Python dependency versions you actually tested for a reproducible result; do not claim reproducibility while leaving runtime dependencies unbounded.

The service process must run in the foreground so Docker can manage its lifecycle. Document the command used to start the API.

## Task 3 — Build and inspect

Build a locally tagged image, then inspect its configuration and run it bound to loopback only. Choose a free local port if 8000 is occupied.

    docker build -t dojo-notes-api:lab02 .
    docker image inspect dojo-notes-api:lab02
    docker run --rm --name dojo-notes-api -p 127.0.0.1:8000:8000 dojo-notes-api:lab02

In another terminal, verify:

    curl --fail http://127.0.0.1:8000/health
    curl --fail http://127.0.0.1:8000/docs

Then exercise create/read/delete against the container and confirm expected status codes. Stop the container with Ctrl-C or docker stop dojo-notes-api. If the image exits, inspect docker logs and docker inspect before changing random settings.

## Task 4 — Security review

Record the evidence for each item:

- The container process is not root.
- The port is published only to 127.0.0.1.
- The image contains no secrets or local environment files.
- The Dockerfile does not embed credentials in ARG or ENV.
- The application returns useful errors without leaking stack traces or configuration.
- The image uses only required runtime dependencies.
- The application data is ephemeral and the limitation is documented.

If a scanner such as Trivy is already installed, scan the image and record its version and findings. Scanner availability is optional; never claim a scan passed if it was not run.

## Exit criteria

- [ ] Notes API tests pass before containerisation.
- [ ] Image builds from a clean context.
- [ ] Health endpoint and notes endpoints respond as expected.
- [ ] Container runs as non-root and is bound to loopback on the host.
- [ ] Image/context review finds no secrets or unnecessary files.
- [ ] Stop and remove the container; confirm no lab container remains running.

## Explain

1. What is the difference between an image and a container?
2. Why does the application listen on 0.0.0.0 inside the container while the host port is bound to 127.0.0.1?
3. Why does a non-root user reduce impact but not eliminate container risk?
4. What data is lost when this in-memory API restarts?
5. What would need to change before a public deployment?

Evidence: Dockerfile and .dockerignore review, sanitized build output, endpoint tests, non-root evidence, and a short limitations note. Do not publish a public endpoint as part of this lab.
