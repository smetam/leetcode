from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, nums[0]
        for reward in nums[1:]:
            prev, curr = curr, max(curr, prev + reward)
        return curr