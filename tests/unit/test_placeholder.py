# tests/unit/test_placeholder.py
# A basic pytest test suite

import pytest

def test_true_is_truthy():
    assert True, "True should be truthy"

def test_sample_math():
    assert 1 + 1 == 2, "Basic arithmetic should work"

@pytest.mark.parametrize("input,expected", [
    (0, 0),
    (1, 1),
    (2, 4),
    (3, 9),
])
def test_square(input, expected):
    def square(x):
        return x * x
    assert square(input) == expected
