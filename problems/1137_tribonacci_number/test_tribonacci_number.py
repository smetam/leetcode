import pytest
from tribonacci_number import Solution

@pytest.mark.parametrize('n, expected', [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 7),
    (25, 1389537),
])
def test_solution(n, expected):

    assert Solution().tribonacci(n) == expected
