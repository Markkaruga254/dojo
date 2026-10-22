# ML curriculum

| Wk | Track | Learn | Build / gate |
|---|---|---|---|
| 1 | A | NumPy, vectors/matrices, gradients (by code), linear + logistic regression | regression from scratch on a toy dataset; plot loss |
| 2 | A | Neural net + backprop from scratch; PyTorch tensors/autograd | 2-layer net on a toy task, gradient-checked |
| 3 | A→B | PyTorch training loop, metrics, over/under-fitting; why tokenisation matters | train/val/test split discipline; confusion matrix by hand |
| 4 | B | BPE, vocab, embeddings, LLM course basics | **lab01 BPE green** |
| 5 | B | Attention, transformer block, pipelines, datasets | **lab02 attention green** |
| 6 | B | Fine-tune a small model with `Trainer` on a free GPU | one fine-tune with a held-out eval, logged honestly |
| 7 | C | Small-model fine-tuning, LoRA/PEFT, evaluation basics | compare full vs LoRA on cost and quality |
| 8 | C | Eval harness, embeddings, vector search, RAG basics | retrieval recall@k on your own test queries |
| 9 | D | Agents: tool use, loops, failure modes | agent that calls two tools; log failures |
| 10 | D/E | Agents continued; context engineering | context budget experiments |
| 11 | Capstone | Hypothesis validation, source inventory, eval plan | `ml/capstone/BRIEF.md` filled in |
| 12 | Capstone | v1: retrieval over authoritative sources; uncertainty + referral behaviour | 30-question test set run |
| 13 | Capstone | Evaluation + red-teaming (hallucination, privacy, safety) | failure report |
| 14 | Interview | Metrics, bias/variance, regularisation, transformers recap | answer `assessments/interview/ml.md` aloud |
| 15 | Interview | ML system design + capstone write-up | one-page design doc |
| 16 | Taper | Capstone polish; Track F only if ahead | published write-up |

## From-scratch checklist (you must be able to code these cold)
linear regression (closed form and gradient descent) · logistic regression · softmax + cross-entropy · a 2-layer MLP with backprop · k-means · train/val/test split · precision/recall/F1/ROC-AUC · BPE · scaled dot-product attention · a mini transformer block (forward pass).

## Evaluation honesty rules
- Never evaluate on training data. Fix the test set before tuning.
- Report the baseline (majority class, keyword search, zero-shot) next to your model.
- Save every run: config, seed, metric, date.
