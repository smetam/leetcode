from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumsum = 0
        max_sum = min(nums)
        for num in nums:
            cumsum = max(cumsum, 0) + num
            if cumsum > max_sum:
                max_sum = cumsum
        return max_sum