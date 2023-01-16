from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = 0, 0
        for idx in range(1, len(cost)):
            prev, curr = curr, min(prev + cost[idx-1], curr + cost[idx])
        return curr
