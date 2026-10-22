"""Lab 02: attention in NumPy."""
from __future__ import annotations

import numpy as np


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Numerically stable softmax (subtract the max along `axis`)."""
    raise NotImplementedError


def scaled_dot_product_attention(q: np.ndarray, k: np.ndarray, v: np.ndarray,
                                 causal: bool = False) -> tuple[np.ndarray, np.ndarray]:
    """q: (Tq, d), k: (Tk, d), v: (Tk, dv). Return (output (Tq, dv), weights (Tq, Tk)).

    scores = q @ k.T / sqrt(d). If causal (Tq == Tk), position i may only attend to j <= i
    (mask future positions before the softmax, e.g. with -inf). weights = softmax(scores, axis=-1).
    """
    raise NotImplementedError
