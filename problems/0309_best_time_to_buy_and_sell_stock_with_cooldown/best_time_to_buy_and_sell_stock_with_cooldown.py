from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        hold, not_hold, cooldown = -prices[0], 0, 0
        for p in prices[1:]:
            hold, not_hold, cooldown = max(hold, not_hold - p), max(not_hold, cooldown), hold + p
        # hold is <= not_hold
        return max(not_hold, cooldown)

