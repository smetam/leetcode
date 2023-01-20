from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        
        hold, not_hold = -prices[0] - fee, 0
        for p in prices:
            hold, not_hold = max(hold, not_hold - p), max(not_hold, hold + p - fee)
        return max(hold, not_hold)