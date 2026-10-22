# Lab 02: Scaled dot-product attention (NumPy)

## Goal

Implement the attention calculation used by transformer models and verify its shape, numerical stability, and causal masking behavior.

## Build

Implement `softmax` and `scaled_dot_product_attention` in `attention.py`.

1. Make softmax numerically stable by subtracting the maximum along the selected axis before exponentiation.
2. Compute scores as `q @ k.T / sqrt(d)`, where `d` is the final dimension of queries and keys.
3. If `causal=True`, mask future positions before softmax. The documented contract only enables causal masking when `Tq == Tk`.
4. Return both the output matrix and attention weights with the documented shapes.

## Verify

Install the optional lab dependencies if needed, then run from this directory:

```bash
python -m pytest -q
```

The supplied tests check large logits, row normalisation, different query/key sequence lengths, causal masking, and a small manual calculation. Add at least one test of your own, such as a non-default softmax axis, a single-key attention row, or a clear assertion about an invalid shape.

## Experiment

Use a fixed random seed and compare attention logits with key/query dimension `d=4` and `d=512`, with and without division by `sqrt(d)`. Print the softmax entropy for each case. Record the setup and observation; do not claim the result proves a universal rule from one random sample.

## Explain and record

- Why subtracting the maximum preserves softmax probabilities while reducing overflow risk.
- Why scaling the dot product affects the sharpness of the softmax distribution.
- What the causal mask prevents, and why it must be applied before softmax.
- The test command, result, added test, and one limitation of this small implementation.

This is a learning implementation, not a full transformer layer. The starter functions are intentionally incomplete until you implement and verify them.
