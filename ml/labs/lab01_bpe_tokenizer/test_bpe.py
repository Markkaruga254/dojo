from bpe import decode, encode, train_bpe


def test_classic_example():
    assert train_bpe("aaabdaaabac", 3) == [("a", "a"), ("a", "b"), ("aa", "ab")]


def test_stops_when_no_repeated_pair():
    assert train_bpe("abcd", 5) == []


def test_zero_merges():
    assert train_bpe("aaaa", 0) == []


def test_encode_applies_merges_in_order():
    merges = [("a", "a"), ("a", "b"), ("aa", "ab")]
    assert encode("aaab", merges) == ["aaab"]
    assert encode("aaa", merges) == ["aa", "a"]
    assert encode("xyz", merges) == ["x", "y", "z"]


def test_roundtrip():
    text = "low lower lowest low low"
    merges = train_bpe(text, 6)
    toks = encode(text, merges)
    assert decode(toks) == text
    assert len(toks) < len(text)
