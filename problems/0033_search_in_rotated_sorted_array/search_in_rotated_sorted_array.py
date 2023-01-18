from typing import List


class Solution:
    @staticmethod
    def find_rotation(nums: List[int]) -> int:
        last_num = nums[-1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= last_num:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def search(self, nums: List[int], target: int) -> int:
        # find rotation position
        split_idx = self.find_rotation(nums)
    
        # fing in which part of nums to search
        if (split_idx > 0) and (target >= nums[0]):
            nums = nums[:split_idx]
            shift = 0
        else:
            nums = nums[split_idx:]
            shift = split_idx
        
        # search
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            value = nums[mid]
            if value == target:
                return mid + shift
            if target < value:
                right = mid - 1
            else:
                left = mid + 1
        return -1