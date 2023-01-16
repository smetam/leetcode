from typing import List


class Solution:
    @staticmethod
    def _rob(nums) -> int:
        prev, curr = 0, nums[0]
        for reward in nums[1:]:
            prev, curr = curr, max(curr, prev + reward)
        return curr

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))