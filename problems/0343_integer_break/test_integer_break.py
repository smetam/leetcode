import pytest
from integer_break import Solution


@pytest.mark.parametrize('n, expected', [
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 6),
    (10, 36),
    (58, 1549681956),
])
def test_solution(n, expected):
    assert Solution().integerBreak(n) == expected
