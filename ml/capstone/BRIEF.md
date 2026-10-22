# Capstone brief: improving access to legal information for Kenyans (working hypothesis)

**Status: hypothesis, not a fixed solution.** The first job (Week 11) is to test whether the problem is real and what the cheapest effective fix is. LLM + RAG, fine-tuning, plain search, a structured FAQ, or a non-ML fix may all be better. Write down which and why.

## Problem statement (draft; sharpen it)

People, especially persons with disabilities, struggle to find clear, trustworthy information about their legal rights and the right place to get help.

## Week 11 deliverables

1. **Users and needs:** 3–5 conversations with real potential users or advocates, or a documented reason you could not conduct them. Ask about information needs, not private case histories. Obtain consent before taking notes; do not publish identifying details.
2. **Source inventory:** authoritative sources only (statutes, official guidance, court/tribunal pages, accredited legal-aid organisations). For each source record URL, licence/terms, update frequency, language, format, and date checked. Verify current legal texts on official sites; do not rely on memory.
3. **Baseline:** evaluate plain keyword search over the same source collection against a small, recorded set of representative questions.
4. **Decision memo (one page):** chosen approach, evidence supporting it, alternatives considered, what will not be built, and unresolved assumptions.

If user conversations are not feasible, label that evidence as missing; do not invent interviews, quotes, or validation.

## Non-negotiable behaviours

- **Grounded:** answers cite the source passage; if no adequate source is retrieved, say so.
- **Uncertainty:** communicate the limits of general information. This tool is not a lawyer and does not provide legal advice.
- **Referral:** specific, urgent, personal, or high-stakes situations should be directed to qualified assistance, such as an advocate or legal-aid organisation.
- **Privacy:** do not store personal case details beyond what the session needs; do not log sensitive text without consent; redact before sharing evaluation material.
- **Accessibility:** use plain language, short answers, screen-reader-friendly structure, and keyboard-accessible controls. Treat SMS, WhatsApp, and voice as optional future interfaces, not prerequisites for a credible first version.
- **Source freshness:** display or record when each source was checked, and make stale or conflicting material visible rather than silently choosing one.

## Technical outline (only if RAG is justified)

ingest → clean/chunk → embed → index → retrieve → answer with citations → refusal/referral policy → evaluation harness → API → container → deployment if affordable.

Start with the smallest baseline that can answer the evaluation questions. Do not add a vector database, agent framework, fine-tuning, or paid service unless the decision memo explains what measurable problem it solves.

## Build gates

| Gate | Required evidence | Stop condition |
|---|---|---|
| Scope and sources | Decision memo, source inventory, baseline query set | Do not build a model before the source and user problem are credible |
| Local prototype | Reproducible setup, representative questions, visible citations, useful no-answer behaviour | If answers cannot be grounded, narrow scope or use search/FAQ instead |
| Evaluation | Versioned held-out and red-team sets, metrics, five analysed failures | Do not tune against the held-out test set or hide failed cases |
| Security and privacy | Threat/risk review, secret scan, redacted fixtures, negative tests | No public demo with exposed secrets or unaddressed critical privacy/safety failures |
| Release decision | Runbook, limits, rollback/cleanup, evidence-linked rubric | Hosting is optional if cost or account access is unavailable; document a local demo and mark deployment deferred |

## Definition of done (Week 16)

A reproducible local or hosted demo, secured API if an API is exposed, source and evaluation report with failures shown, documented limitations and referral behaviour, and a one-page write-up with evidence. If deployed, include the endpoint, date checked, cost assumptions, access controls, rollback, and teardown steps. **Never claim a deployment, user validation, or evaluation result that has not happened.**
