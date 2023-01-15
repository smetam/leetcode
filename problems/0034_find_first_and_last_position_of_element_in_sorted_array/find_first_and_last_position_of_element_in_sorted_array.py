from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # search first elem >= target
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        start = left

        # search first elem > target
        left, right = start, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target + 1 <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        end = left

        # start == end means, target is not in nums
        if start >= end:
            return -1, -1
        return start, end - 1

