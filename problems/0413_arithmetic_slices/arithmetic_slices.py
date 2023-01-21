from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        arithmetic_slices = 0
        diff = nums[1] - nums[0]
        slice_len = 2
        for prev, curr in zip(nums[1:], nums[2:]):
            new_dff = curr - prev
            if new_dff == diff:
                slice_len += 1
            else:
                if slice_len >= 3:
                    arithmetic_slices += (slice_len - 2) * (slice_len - 1) // 2
                slice_len = 2
                diff = new_dff
        if slice_len >= 3:
            arithmetic_slices += (slice_len - 2) * (slice_len - 1) // 2
        return arithmetic_slices