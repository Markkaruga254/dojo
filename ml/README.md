# Machine-learning track

This track combines foundations, official Hugging Face learning material, from-scratch implementation labs, and a capstone. The goal is not to finish every available course; it is to understand mechanisms, apply selected material, and produce verifiable project evidence.

## Learning sequence

1. **A — Foundations:** NumPy, tensors, gradients, regression, neural networks, and training loops. These are local exercises, not a separate Hugging Face course.
2. **B — LLM foundations:** use the [official Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter0/1) as the main conceptual backbone. Follow the selected chapter plan in the syllabus map.
3. **C — Post-training:** use the [Hugging Face smol-course](https://huggingface.co/learn/smol-course/unit0/1) for selected instruction-tuning and evaluation work. Check the current unit list and hardware requirements before scheduling.
4. **D — Agents:** use the [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction) for tool use, agent workflows, and evaluation.
5. **E — Context engineering:** the Context Course is optional enrichment when it directly supports the capstone and the official unit structure has been checked.
6. **F — Deep reinforcement learning:** the Deep RL Course is optional. Skip it if interview preparation or capstone gates are behind.

The source courses evolve. Keep chapter selection and completion status in [the syllabus map](../docs/HF_SYLLABUS_CHECK.md); do not mark a track complete just because you opened its landing page.

## How to study a unit

**Read the official lesson → explain it from memory → implement a small mechanism or run a controlled experiment → test/evaluate → record the result and limitation.** Use AI to review reasoning and explain errors, not to conceal gaps by copying a complete solution.

## Constraints

- Assume no dedicated GPU. Prefer small experiments, CPU-friendly exercises, and free hosted notebooks where available.
- Check compute limits, privacy, and service terms before uploading data or using hosted notebooks.
- Never evaluate on training data. Keep a fixed test set and report a simple baseline beside model results.
- Record configuration, seed where relevant, metrics, date, and known limitations.

## Track contents

- CURRICULUM.md — weekly learning plan and gates.
- CHECKPOINTS.md — evidence required for foundations, implementation labs, evaluation, and the capstone.
- labs/ — from-scratch implementation labs, including BPE tokenization and attention.
- capstone/ — project brief, evaluation plan, and risk register.

Some starter functions are intentionally incomplete. That is part of the exercise, not a defect to hide. Follow each lab's instructions and verify your implementation with the provided and additional tests.

Start with [ML checkpoints](CHECKPOINTS.md), then follow [the selected Hugging Face unit map](../docs/HF_SYLLABUS_CHECK.md).
