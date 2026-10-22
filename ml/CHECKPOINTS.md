# Machine-learning checkpoints

This track is deliberately split between official course study and local implementation. Course completion badges are useful signals, but the local checkpoints require you to demonstrate understanding and evaluation discipline.

## Gate A — foundations (Weeks 1–3)

- [ ] Explain arrays/tensors, shapes, gradients, and train/validation/test splits.
- [ ] Implement a small regression model and plot the loss curve.
- [ ] Implement a two-layer toy network or use PyTorch autograd and compare gradients.
- [ ] Explain overfitting and give one example of data leakage.

**Evidence:** runnable small experiment, recorded configuration, a short explanation, and a note on limitations.

## Gate B — tokenization and attention (Weeks 4–5)

- [ ] Complete the BPE tokenizer lab in labs/lab01_bpe_tokenizer and run its tests.
- [ ] Explain each BPE merge with a tiny worked example.
- [ ] Complete the attention lab in labs/lab02_attention and run its tests.
- [ ] Verify attention tensor shapes and test a simple numerical example.
- [ ] Compare the from-scratch implementation with the relevant official Hugging Face lesson or library behaviour.

**Evidence:** tests, a small hand-checkable example, and a brief explanation written without notes.

These starter labs are intentionally incomplete. Do not mark the gate green until your implementation and tests pass.

## Gate C — use and evaluation (Weeks 6–8)

- [ ] Load a small model and dataset with the official Hugging Face libraries.
- [ ] Fix a held-out test set before tuning.
- [ ] Report a simple baseline next to any fine-tuned result.
- [ ] Record model/dataset identifier, configuration, seed when applicable, metrics, runtime, and memory/cost constraints.
- [ ] Show at least five failure examples and explain whether they come from data, retrieval, prompting, or model limitations.

If compute is unavailable, complete a small CPU-friendly or mocked workflow and document what could not be validated. Never incur charges just to make a gate look complete.

## Gate D — agents and capstone (Weeks 9–13)

- [ ] Build a small tool-using agent with deterministic tools and explicit stopping conditions.
- [ ] Log tool errors and handle malformed or missing tool results.
- [ ] Build a fixed evaluation set before tuning.
- [ ] Test unsupported questions, missing sources, prompt injection, stale/conflicting evidence, and privacy boundaries.
- [ ] Report a keyword-search baseline and the five worst failures.
- [ ] Use the capstone brief, evaluation plan, and [capstone rubric](../assessments/CAPSTONE-RUBRIC.md).

## Definition of a completed unit

Record the official unit URL, sections actually completed, local exercise that applies it, verification output, and unresolved gap. Opening a course page is not completion. See [the Hugging Face syllabus map](../docs/HF_SYLLABUS_CHECK.md) for the selected-unit mapping.
