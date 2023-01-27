import pytest
from coin_change_ii import Solution


@pytest.mark.parametrize('amount, coins, expected', [
    (5, [1,2,5], 4),
    (5, [1], 1),
    (5, [1, 2], 3),
    (3, [2], 0),
    (10, [10], 1),
])
def test_solution(amount, coins, expected):
    assert Solution().change(amount, coins) == expected
