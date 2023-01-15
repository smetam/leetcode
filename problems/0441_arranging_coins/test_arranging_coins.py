import pytest
from arranging_coins import Solution


@pytest.mark.parametrize('n, expected', [
    (5, 2),
    (8, 3),
    (10, 4),
    (15, 5),
    (16, 5),
])
def test_solution(n, expected):
    assert Solution().arrangeCoins(n) == expected
