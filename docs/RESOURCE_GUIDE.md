# Free-first resource guide

This guide maps external learning material to the work already scheduled in Dojo. Use it as a **just-in-time reference**, not another syllabus to complete. The local curriculum, labs, and checkpoints remain the source of truth.

## How to use resources without losing the course

1. Open the current week's task in [ROADMAP.md](../ROADMAP.md) and the relevant track's curriculum/checkpoints.
2. Try the local task first for 20–30 minutes. Write down the specific concept or error you cannot resolve.
3. Open **one** relevant resource below; study only the section that answers that question.
4. Return to the Dojo task, implement it yourself, run tests, and explain the result without notes.
5. Record the resource section, commit/test/evaluation evidence, and what remains unclear in your daily log.

Prefer official docs and free materials. A course being free to read does not mean its hosted compute, API usage, datasets, or cloud deployment are free. Never add a paid subscription or provision a billable resource just to keep the schedule moving.

## Route by course stage

| When you are here | Start with | Use it for | Return to Dojo and prove |
|---|---|---|---|
| Setup / every week | [The Missing Semester](https://missing.csail.mit.edu/) and [Pro Git](https://git-scm.com/book/en/v2) | Shell, command-line workflows, Git fundamentals | A clean local commit, understandable diff, and useful learning log |
| Weeks 1–4: Python foundations and practical code | [Official Python tutorial](https://docs.python.org/3/tutorial/) → [CS50P](https://cs50.harvard.edu/python/) when you need a fuller beginner explanation | Language fundamentals, functions, exceptions, files, tests | Complete the matching [Python lab](../python/) and add an edge-case test |
| Weeks 1–12: DSA | [VisuAlgo](https://visualgo.net/en) for animations; [CP-Algorithms](https://cp-algorithms.com/) for deeper explanations; [LeetCode](https://leetcode.com/problemset/) for practice | Understand a pattern before coding; check constraints and complexity | Solve or retry a problem independently, explain complexity, and update the [DSA tracker guidance](../dsa/README.md) |
| Weeks 1–2: ML prerequisites | [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) and [PyTorch tutorials](https://pytorch.org/tutorials/) | Arrays/tensors, gradients, autograd, training loops | Implement a small example and record expected vs actual output |
| Weeks 3–8: LLMs, tokenization, attention, fine-tuning | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter0/1), then the exact chapter in the [Dojo syllabus map](HF_SYLLABUS_CHECK.md) | Learn only the concepts linked to this week's BPE, attention, datasets, or model task | Finish the local lab, tests/experiment, and explanation; opening a course unit is not completion |
| Weeks 7–12: instruction tuning, evaluation, agents | [Hugging Face smol-course](https://huggingface.co/learn/smol-course/unit0/1) and [Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction) | Selected post-training, evaluation, and tool-use topics | Record dataset/model versions, evaluation method, limitations, and actual results |
| Weeks 1–6: cloud foundations | [Linux Journey](https://linuxjourney.com/), [Pro Git](https://git-scm.com/book/en/v2), [Docker Get Started](https://docs.docker.com/get-started/), [GitHub Actions quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart), [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials) | Linux/Git, containers, CI, Terraform lifecycle in the same order as the local labs | Complete the matching [Cloud lab sequence](../cloud/README.md#lab-sequence); use local exercises before any cloud spend |
| Weeks 1–8: NSE platform build | [pandas getting started](https://pandas.pydata.org/docs/getting_started/index.html), [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/), [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/), [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) | Data ingestion, API design, persistence, and testable increments | Complete a small vertical slice with tests, source/provenance notes, and a failure case |
| Assessment / mock weeks | [Practical assessment playbook](../assessments/PRACTICAL-ASSESSMENT-PLAYBOOK.md) and the relevant track checkpoints | Practise under the real time/tool constraints, not while reading a tutorial | Save the score, missed concepts, retrospective, and scheduled re-solves |

## Track-specific resource shelves

### DSA and interview problem solving

- [VisuAlgo](https://visualgo.net/en) — free visualisations to build intuition for sorting, trees, graphs, and data structures.
- [CP-Algorithms](https://cp-algorithms.com/) — deeper reference for algorithms and complexity; use only the article relevant to your current pattern.
- [LeetCode problem set](https://leetcode.com/problemset/) — the free problem set is enough to start; premium questions are not required for the core plan.
- [Python built-in data types](https://docs.python.org/3/library/stdtypes.html) — verify actual list, dict, set, tuple, and heap-adjacent behaviour instead of memorising snippets.

**Use this sequence:** attempt → brute force → complexity → pattern hint → optimise → test edge cases → log independent/hinted/assisted status → re-solve after 3/7/21 days.

### Applied Python

- [Official Python tutorial](https://docs.python.org/3/tutorial/) — primary language reference.
- [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) — free structured explanations and exercises.
- [pytest documentation](https://docs.pytest.org/en/stable/) — tests, fixtures, and parametrisation for the local labs.
- [Exercism Python track](https://exercism.org/tracks/python) — optional extra practice; do not let side exercises displace the current Dojo lab.

**Use this sequence:** read the lab brief → write an edge-case test → implement the smallest change → run lab tests → explain one design trade-off.

### Machine learning and Hugging Face

- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter0/1) — primary course for selected transformer/tokenizer concepts.
- [Hugging Face smol-course](https://huggingface.co/learn/smol-course/unit0/1) — selected post-training and evaluation topics.
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction) — agent/tool-use topics when scheduled.
- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html) and [PyTorch tutorials](https://pytorch.org/tutorials/) — prerequisites and small experiments.
- [fast.ai Practical Deep Learning](https://course.fast.ai/) — optional free alternative explanation when a concept is not clicking; it is not a replacement for the mapped Dojo lab.

Do not train a large model to prove progress. Prefer a small CPU-friendly experiment or a free hosted option only after checking current limits. Log dataset/model versions, split strategy, baseline, metric, runtime, and limitations.

### Cloud and DevOps

- [The Missing Semester](https://missing.csail.mit.edu/) — shell, tooling, debugging, and command-line fundamentals.
- [Pro Git](https://git-scm.com/book/en/v2) — version control and branch workflows.
- [Docker Get Started](https://docs.docker.com/get-started/) — images, containers, networking, and volumes.
- [GitHub Actions documentation](https://docs.github.com/en/actions) — workflow syntax, events, permissions, and CI.
- [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials) — configuration, plan/apply/destroy, state, and providers.
- [AWS Skill Builder](https://skillbuilder.aws/) — check the current free learning catalogue; paid subscriptions and live cloud resources are optional, not course requirements.

Do the local Dojo labs first. Before any cloud deployment, check current pricing/quotas, define a teardown plan, avoid committing credentials/state/plans, and verify resources are actually removed. Free tier is not a guarantee of zero cost.

### NSE market-insights platform

- [pandas getting started](https://pandas.pydata.org/docs/getting_started/index.html) — data loading and transformation.
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) — request validation, routes, and dependency patterns.
- [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) and [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) — persistence and querying.
- Use the project’s own [data-source inventory](../nse_platform/DATA_SOURCES.md), [evaluation plan](../nse_platform/EVAL.md), and [compliance notes](../nse_platform/COMPLIANCE.md) before choosing feeds or making claims.

Respect each provider's licence, terms, rate limits, and attribution requirements. A successful ingestion run does not establish source accuracy; record freshness, missing data, duplicates, and failure behaviour. Treat outputs as information, not personal investment advice.

## If you are stuck

- **You cannot explain the concept:** return to the relevant official tutorial section, then explain it from memory in your log.
- **You understand it but cannot implement it:** reduce the task to a tiny input/output example and write a test first.
- **The tests fail:** read the full traceback, reproduce one failure, and inspect the smallest relevant code path.
- **The schedule is slipping:** follow the current gate in [ROADMAP.md](../ROADMAP.md), reduce optional enrichment, and repeat the weak area. Do not add hours or subscriptions by default.
- **A link or course unit has changed:** report it in an issue/PR with the replacement and date checked. Do not silently claim a unit was completed.

## Resource maintenance

Links are curated starting points, not endorsements or guarantees that every third-party service remains free. Re-check official course pages when you start a block. Keep this guide focused: add a resource only when it supports a specific Dojo objective, lab, checkpoint, or documented blocker.
