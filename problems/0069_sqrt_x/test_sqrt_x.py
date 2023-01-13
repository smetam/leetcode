import pytest
from sqrt_x import Solution


@pytest.mark.parametrize('x, expected', [
    (4, 2),
    (8, 2),
    (9, 3),
    (1, 1),
])
def test_solution(x, expected):
    assert Solution().mySqrt(x) == expected
