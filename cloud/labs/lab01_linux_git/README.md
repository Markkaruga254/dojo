# Lab 01: Linux CLI and Git workflow

## Goal

Inspect a local development environment, create a repeatable workspace, review a Git change, and make a local commit. This lab requires no cloud credentials, paid services, root access, or system configuration changes.

## Prerequisites

- Bash or a compatible shell
- Git
- Python 3.11+ for the optional local HTTP-server task

Verify tools:

    git --version
    python3 --version
    pwd

If a command is missing, note your operating system and the missing tool. Do not run copied commands with sudo unless you understand why elevated privileges are required.

## Task 1 — Inspect, don't guess

Run each command and explain what its output tells you:

    pwd
    id
    df -h .
    free -h
    ps -eo pid,comm,%cpu,%mem --sort=-%mem | head
    ss -ltn

If free or ss is unavailable, note that and use an equivalent tool. Do not kill processes or change firewall rules.

**Evidence:** record the command, one observation, and what you would investigate next. Sanitise usernames, hostnames, IP addresses, and process details before sharing output publicly.

## Task 2 — Build a repeatable workspace

From the repository root:

    mkdir -p .local-lab/linux-git
    cd .local-lab/linux-git
    printf 'dojo linux-git lab\n' > README.txt
    printf 'status=ok\n' > app.env.example
    git init
    git status --short

Inspect the untracked files. Add a project-level ignore rule for local lab artifacts and real environment files before committing. If the repository already has a .gitignore, inspect and edit it rather than blindly appending duplicate rules. Keep the example file tracked and never place real credentials in either file.

    cd "$(git rev-parse --show-toplevel)"
    git status --short
    git check-ignore -v .env

Confirm that .env is ignored and that no real environment file or credential is staged.

## Task 3 — Practise a safe Git change

Use a dedicated local branch if working in an existing clone. Do not commit directly to a shared branch.

    git switch -c lab/linux-git-notes
    git status --short
    git diff --check
    git diff -- .gitignore

Create a short note under .local-lab/linux-git/ containing the commands you ran, one observation from the system inspection, one follow-up diagnostic command, and any platform differences.

Review before staging:

    git status --short
    git diff --check
    git diff -- .gitignore

Stage only the intended files, review the staged diff, and commit locally:

    git add .gitignore .local-lab/linux-git/
    git diff --cached --check
    git diff --cached
    git commit -m "docs: record Linux and Git lab observations"
    git status --short
    git log -1 --oneline

Do not push raw system output publicly unless it has been reviewed and sanitised. A local commit is sufficient evidence for this lab.

## Task 4 — Verify a local service (optional)

This task uses loopback only and does not provision a cloud resource. In a temporary directory, start a local-only server:

    mkdir -p /tmp/dojo-http-check
    printf 'dojo local check\n' > /tmp/dojo-http-check/index.html
    cd /tmp/dojo-http-check
    python3 -m http.server 8765 --bind 127.0.0.1

In a second terminal:

    curl --fail http://127.0.0.1:8765/
    ss -ltn | grep 8765

Expected: the response contains “dojo local check”, and the listener is bound to 127.0.0.1 rather than a public interface. Stop the server with Ctrl-C and confirm the listener is gone. If port 8765 is occupied, choose another unused high port consistently.

## Exit criteria

- [ ] Explain the current directory, disk space, memory, processes, and listening TCP ports in your own words.
- [ ] Make a local Git commit after reviewing the staged diff.
- [ ] Demonstrate that environment secrets are not staged.
- [ ] If you ran the optional server, show that it responds locally and is stopped afterward.
- [ ] Record one mistake or surprise, its cause, and the command that helped diagnose it.

## Reflection

1. Why is reviewing the staged diff safer than committing without inspection?
2. What is the difference between a process and a listening socket?
3. Why bind the optional server to 127.0.0.1?
4. Which output would you redact before sharing a troubleshooting note publicly?

**Evidence format:** commands, expected and actual result, short explanation, and a sanitised terminal excerpt if useful. Do not claim a task passed if you did not run it.
