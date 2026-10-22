# Roadmap: 16 weeks + setup

Week 1 starts **Mon 26 Oct 2026**. Week 16 ends **Sun 14 Feb 2027**. Day 90 (from 23 Oct) falls in Week 13.
Assessments (Safaricom / Andela) are expected around mid-February: confirm the dates and formats from your invitations and update `assessments/mocks/SCHEDULE.md`.

| Phase | Weeks | Focus |
|---|---|---|
| 0 Setup | 23–25 Oct | Environment, diagnostic, first log |
| 1 Foundations + Build I | 1–4 | DSA basics, Python fundamentals → backend, ML Track A, platform data ingestion |
| 2 Build II | 5–8 | Trees/heaps/backtracking/graphs, auth + data, HF Track B/C, platform sentiment + briefs |
| 3 Assessment intensification | 9–12 | Hard DSA patterns, Python interview core, SQL, agents, capstone build. Platform = maintenance only (≤1h/wk) |
| 4 Sharpen + taper | 13–16 | Timed mixed sets, weekly mocks, capstone eval/deploy/write-up, taper in Week 16 |
| After | 17+ | Platform commercialisation + public trading journey (see `nse_platform/`) |

Week 9 contains Christmas: plan it as a ~70% load week and say so in the log.

## Gates (objective: all must be true to pass)
**G1 — end Week 4**
- ≥ 40 DSA attempts logged; ≥ 60% of easy/medium solved *independent*
- Python labs 01–04 green; BPE lab green
- Platform: prices + news ingest run unattended for 7 consecutive days
- Mock 1 taken and retro written

**G2 — end Week 8**
- ≥ 90 DSA attempts; trees, heaps, backtracking, graphs each ≥ 6 solved
- Attention lab green; one small model fine-tuned and evaluated on a held-out set
- Platform: hand-labelled eval set (100 items) and a daily brief generated automatically
- Mocks 2–3 retros written

**G3 — end Week 12**
- ≥ 150 DSA attempts; ≥ 20 re-solves from the spaced-repetition queue
- Capstone v1 answers a fixed 30-question test set with sources and refuses appropriately
- Timed mock: 2 problems / 90 min, both with correct brute force, ≥ 1 fully passing

**G4 — Week 16 (go / no-go for assessment week)**
- Last 3 mocks ≥ target on the rubric (`assessments/mocks/RUBRIC.md`)
- Capstone deployed behind a secured API, write-up published
- Environment dry-run done: editor, language, allowed libraries, internet, power, timing

If a gate fails: do **not** add hours. Repeat the weak area for 3–5 days, re-test, then continue.
