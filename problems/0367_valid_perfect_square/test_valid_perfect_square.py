import pytest
from valid_perfect_square import Solution


@pytest.mark.parametrize('num, expected', [
    (16, True),
    (14, False),
    (1, True),
    (25, True),
    (2, False),
])
def test_solution(num, expected):
    assert Solution().isPerfectSquare(num) == expected
