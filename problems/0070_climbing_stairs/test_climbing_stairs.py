import pytest
from climbing_stairs import Solution


@pytest.mark.parametrize('n, expected', [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
])
def test_solution(n, expected):
    assert Solution().climbStairs(n) == expected
