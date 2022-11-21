import pytest
from src.fib import fibonacci


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fib(n, expected):
    result = fibonacci(n=n)
    assert result == expected
