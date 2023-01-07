import pytest
from fibonacci_number import Solution

@pytest.mark.parametrize('n, expected', [
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
])
def test_solution(n, expected):

    assert Solution().fib(n) == expected
