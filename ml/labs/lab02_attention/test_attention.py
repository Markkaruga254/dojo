import numpy as np
from attention import scaled_dot_product_attention, softmax


def test_softmax_stable_and_normalised():
    out = softmax(np.array([1000.0, 1000.0]))
    assert not np.isnan(out).any()
    assert np.allclose(out, [0.5, 0.5])
    m = softmax(np.array([[1.0, 2.0, 3.0], [0.0, 0.0, 0.0]]))
    assert np.allclose(m.sum(axis=-1), 1.0)


def test_shapes_and_rows_sum_to_one():
    rng = np.random.default_rng(0)
    q, k, v = rng.normal(size=(3, 4)), rng.normal(size=(5, 4)), rng.normal(size=(5, 2))
    out, w = scaled_dot_product_attention(q, k, v)
    assert out.shape == (3, 2) and w.shape == (3, 5)
    assert np.allclose(w.sum(axis=-1), 1.0)


def test_causal_mask():
    rng = np.random.default_rng(1)
    x = rng.normal(size=(4, 3))
    out, w = scaled_dot_product_attention(x, x, x, causal=True)
    assert np.allclose(np.triu(w, k=1), 0.0)
    assert np.allclose(w.sum(axis=-1), 1.0)
    assert np.allclose(out[0], x[0])  # first position can only see itself


def test_matches_manual_computation():
    q = np.array([[1.0, 0.0]])
    k = np.array([[1.0, 0.0], [0.0, 1.0]])
    v = np.array([[10.0], [20.0]])
    out, w = scaled_dot_product_attention(q, k, v)
    s = np.array([1.0, 0.0]) / np.sqrt(2)
    e = np.exp(s - s.max())
    expected_w = e / e.sum()
    assert np.allclose(w[0], expected_w)
    assert np.allclose(out[0], expected_w @ v[:, 0])
