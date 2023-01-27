from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0 for _ in range(target)]
        for curr in range(1, target + 1):
            ways = [dp[curr-num] if curr-num >= 0 else 0 for num in nums]
            dp[curr] = sum(ways)
        return dp[-1]