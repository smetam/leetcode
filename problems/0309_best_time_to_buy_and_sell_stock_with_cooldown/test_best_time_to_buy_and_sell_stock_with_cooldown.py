import pytest
from best_time_to_buy_and_sell_stock_with_cooldown import Solution


@pytest.mark.parametrize('prices, expected', [
    ([1,2,3,0,2], 3),
    ([1], 0),
    ([4,3,2,10,11,0,11], 19)
])
def test_solution(prices, expected):
    assert Solution().maxProfit(prices) == expected
