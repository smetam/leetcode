from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for idx, num in enumerate(nums):
            if max_reach < idx:
                return False
            max_reach = max(max_reach, idx + num)
        return max_reach >= n - 1