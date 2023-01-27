import pytest
from perfect_squares import Solution


@pytest.mark.parametrize('n, expected', [
    (12, 3),
    (13, 2),
    (1, 1),
    (25, 1),
    (10000, 1),
    (9999, 4),
    (442, 2),
])
def test_solution(n, expected):
    assert Solution().numSquares(n) == expected
