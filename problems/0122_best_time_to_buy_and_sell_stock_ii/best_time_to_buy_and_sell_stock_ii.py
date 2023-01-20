from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        for prev_price, price in zip(prices[0:-1], prices[1:]):
            diff = max(0, price - prev_price)
            profit += diff
        return profit


