import pytest
from coin_change import Solution


@pytest.mark.parametrize('coins, amount, expected', [
    ([1,2,5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1,3,5], 8, 2),
])
def test_solution(coins, amount, expected):
    assert Solution().coinChange(coins, amount) == expected
