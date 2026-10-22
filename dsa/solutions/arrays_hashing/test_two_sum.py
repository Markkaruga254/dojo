from two_sum import two_sum


def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]


def test_negative_and_zero():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]


def test_no_solution():
    assert two_sum([1, 2, 3], 100) == []
