from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = list(sorted(nums))
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            n_elements_to_right = len(nums) - mid - 1
            if n_elements_to_right <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        n_elements_to_right = len(nums) - right - 1
        print(nums, right, n_elements_to_right)
        if n_elements_to_right == 0 or n_elements_to_right > nums[right + 1]:
            return -1
        return n_elements_to_right
