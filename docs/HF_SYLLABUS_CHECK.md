# Hugging Face curriculum map

This map connects the local 16-week plan to selected units in the official Hugging Face courses. The official syllabus changes over time; re-check the linked table of contents when starting each unit. This repository links to course material and provides original exercises; it does not copy official lesson text or notebooks.

## Week-by-week source-to-practice map

| Local week | Official source and selected units | Local practice / evidence | Scope |
|---|---|---|---|
| 1 | Local foundations: NumPy arrays, vectors/matrices, gradients, regression | Implement regression on toy data; plot loss and explain the gradient update | Prerequisite work; not a Hugging Face course unit |
| 2 | Local foundations: neural networks, backpropagation, PyTorch tensors/autograd | Two-layer network on a toy task; check gradients and explain train/eval mode | Prerequisite work; not a Hugging Face course unit |
| 3 | [LLM Course, Chapter 1: Transformer models](https://huggingface.co/learn/llm-course/en/chapter1/1) — skim the concepts needed for tokenisation and attention | Training/validation/test split discipline; explain tokens, embeddings, attention, and leakage in your own words | Read for concepts; do not attempt to master every transformer detail in one week |
| 4 | [LLM Course, Chapter 6: Tokenizers](https://huggingface.co/learn/llm-course/en/chapter6/1) plus relevant parts of Chapter 1 | `ml/labs/lab01_bpe_tokenizer`: BPE merges, vocabulary, encode/decode tests; write a short comparison with the official tokenizer tooling | Core implementation gate: BPE lab green |
| 5 | [LLM Course, Chapter 1: Transformer models](https://huggingface.co/learn/llm-course/en/chapter1/1), [Chapter 2: Using Transformers](https://huggingface.co/learn/llm-course/en/chapter2/1), and [Chapter 5: Datasets](https://huggingface.co/learn/llm-course/en/chapter5/1) | `ml/labs/lab02_attention`: scaled dot-product attention; run a small Transformers pipeline and load/split a small dataset | Core implementation gate: attention lab green; no large-model training required |
| 6 | [LLM Course, Chapter 3: Fine-tuning a pretrained model](https://huggingface.co/learn/llm-course/en/chapter3/1); consult [Chapter 4: Sharing models and tokenizers](https://huggingface.co/learn/llm-course/en/chapter4/1) only if publishing a model artifact | Fine-tune a small model only if compute and dataset size allow; fix held-out evaluation data before tuning and record the baseline, runtime, memory, and results | Use a small CPU-friendly or free hosted run; skip a costly run rather than incur charges |
| 7 | [smol-course, Unit 1: Instruction Tuning](https://huggingface.co/learn/smol-course/unit1/1) and the course's current evaluation unit | Compare a small baseline with a tuned result where feasible; record dataset, prompt/chat template, metric, and limitations | Selected units, not a claim of full course completion |
| 8 | [smol-course, Unit 4: Model Evaluation](https://huggingface.co/learn/smol-course/unit4/1); optionally study preference alignment only after the evaluation baseline is sound | Create a repeatable evaluation harness and compare quality, latency, and cost; report failure examples | Evaluation first; preference alignment is optional if behind schedule |
| 9 | [Agents Course, Unit 1: Introduction to Agents](https://huggingface.co/learn/agents-course/en/unit1/introduction) | Build a small tool-using agent with at least two deterministic tools; log tool calls, errors, and termination conditions | Core agent fundamentals; do not add tools without a clear need |
| 10 | [Agents Course, Unit 2: Frameworks](https://huggingface.co/learn/agents-course/en/unit2/introduction) and [Unit 3: Agentic RAG use case](https://huggingface.co/learn/agents-course/en/unit3/introduction) | Compare a simple hand-written loop with one framework or retrieval workflow; document failure cases and why the abstraction helps | Choose one framework; do not learn three frameworks in parallel |
| 11–13 | Revisit only source units needed for the capstone; use the official evaluation/agent observability material if applicable | User/problem validation, source inventory, fixed evaluation set, baseline, red-team tests, and failure report | The capstone's evidence and safety are the priority, not collecting more course completions |
| 14–16 | Review relevant LLM fundamentals and selected course notes | Explain transformers, tokenisation, evaluation, data leakage, tool use, and limitations without notes; link explanations to capstone evidence | Revision and project delivery; no new course track by default |

### Optional material — defer by default

- [smol-course, Unit 2: Preference Alignment](https://huggingface.co/learn/smol-course/unit2/1): study only after instruction-tuning and evaluation fundamentals are understood.
- [smol-course, Unit 3: Vision Language Models](https://huggingface.co/learn/smol-course/unit3/1): optional and not required by the current text-focused capstone.
- [Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction) bonus units: observability/evaluation is relevant when it helps the capstone; other bonus units are optional.
- [Deep RL Course](https://huggingface.co/learn/deep-rl-course/en/unit0/introduction) and the [Context Course](https://huggingface.co/learn/context-course): enrichment only. Do not schedule these until the interview and capstone gates are on track and the official unit structure has been checked.

## Unit completion record

For each unit actually studied, add a dated record to your learning log with:

1. Official URL and unit title.
2. Specific sections completed (not just the landing page).
3. Local note, lab, experiment, or project change that applies the concepts.
4. Verification: quiz, test, evaluation metric, or explanation written from memory.
5. Status: not started, in progress, completed, or deferred. **Completed** means practice and verification were done.

## Budget and environment rules

- Python and DSA interview preparation remain protected priorities.
- Assume no dedicated GPU. Prefer small datasets, small models, CPU-friendly tasks, or a free hosted notebook when its terms and limits are suitable.
- Never upload private or sensitive data to a hosted notebook or model service without authorisation and an explicit data-handling review.
- Before fine-tuning, record estimated compute/time and the fallback if the run is too expensive or slow.
- Never evaluate on training data. Fix the held-out test set before tuning and compare with a simple baseline.
- Record the seed where relevant, model/dataset identifier and revision, configuration, metrics, date, and limitations.

## Verification state

The mapping above was checked against the official Hugging Face course navigation on 22 October 2026. Course contents can change, and this is a **selected-unit plan**, not a claim that the learner has completed these units or that every course chapter is mapped. Re-check unit availability before starting each block and update the record if the official syllabus changes.
