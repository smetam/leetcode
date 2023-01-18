from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if all(num < 0 for num in nums):
            return max(nums)

        max_sum, min_sum = min(nums), max(nums)
        max_cumsum, min_cumsum = 0, 0
        # find max subarray, min subarray
        for num in nums:
            max_cumsum = max(max_cumsum, 0) + num
            min_cumsum = min(min_cumsum, 0) + num
            max_sum = max(max_sum, max_cumsum)
            min_sum = min(min_sum, min_cumsum)

        # max circular subarray is either max subarray or complementary to min subarray
        return max(max_sum, sum(nums) - min_sum)