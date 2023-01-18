from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        last_num = nums[-1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= last_num:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]