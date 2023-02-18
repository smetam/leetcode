from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for idx, num in enumerate(nums):
            right_sum = total_sum - num - left_sum
            if left_sum == right_sum:
                return idx
            left_sum += num

        return -1

