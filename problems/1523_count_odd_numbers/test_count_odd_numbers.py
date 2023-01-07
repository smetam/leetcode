import pytest
from count_odd_numbers import Solution


@pytest.mark.parametrize('low, high, expected', [
    (3, 7, 3),
    (8, 10, 1),
    (2, 2, 0),
])
def test_solution(low, high, expected):
    assert Solution().countOdds(low, high) == expected
