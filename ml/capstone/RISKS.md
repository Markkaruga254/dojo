# Risk register
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Outdated or wrong legal content | M | H | Official sources only; store retrieval date; show date in answers |
| Hallucinated citation | M | H | Cite only retrieved passages; verify automatically that quoted text exists in source |
| User treats output as legal advice | H | H | Clear framing, referral policy, no outcome predictions |
| Privacy leak of case details | L | H | No persistent chat logs by default; redaction; minimal retention |
| Scope creep | H | M | Decision memo lists what is out of scope |
| Compute limits | H | M | Small/open models, free tiers, cache embeddings |
