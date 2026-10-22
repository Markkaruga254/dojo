# Capstone brief: improving access to legal information for Kenyans (working hypothesis)

**Status: hypothesis, not a fixed solution.** The first job (Week 11) is to test whether the problem is real and what the cheapest effective fix is. LLM + RAG, fine-tuning, plain search, a structured FAQ, or a non-ML fix may all be better. Write down which and why.

## Problem statement (draft; sharpen it)
People, especially persons with disabilities, struggle to find clear, trustworthy information about their legal rights and the right place to get help.

## Week 11 deliverables
1. **Users & needs:** 3–5 conversations with real potential users or advocates (or a documented reason you could not). What questions do they actually ask?
2. **Source inventory:** authoritative sources only (statutes, official guidance, court/tribunal pages, accredited legal-aid organisations). For each: URL, licence/terms, update frequency, language, format. Verify current legal texts on official sites; do not rely on memory.
3. **Baseline:** what does a plain keyword search over the same sources achieve on your test queries?
4. **Decision memo (1 page):** approach, why, what you will *not* build.

## Non-negotiable behaviours
- Grounded: answers cite the source passage; no source → say so.
- Communicates uncertainty and the limits of general information. It is not legal advice.
- Refers users to qualified help (advocates, legal aid) when a situation is specific, urgent or high-stakes.
- Privacy: no storing of personal case details beyond what the session needs; no logging of sensitive text without consent; redact before any evaluation sharing.
- Accessibility: plain language, short answers, screen-reader-friendly output; consider SMS/WhatsApp/voice later.

## Technical outline (if RAG is the chosen path)
ingest → clean/chunk → embed (open model) → vector index (FAISS or SQLite/pgvector) → retrieve → answer with citations → refusal/referral policy → evaluation harness → API (FastAPI) → container → deploy with CI.

## Definition of done (Week 16)
Deployed behind a secured API, documented limits, evaluation report with failures shown, 1-page write-up published.
