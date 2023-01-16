import pytest
from sum_of_square_numbers import Solution


@pytest.mark.parametrize('c, expected', [
    (5, True),
    (3, False),
    (25, True),
    (4, True),
    (0, True),
])
def test_solution(c, expected):
    assert Solution().judgeSquareSum(c) == expected
