from typing import List


class Solution:

    @staticmethod
    def find_start_index(nums):
        previous = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i]) > abs(previous):
                return i - 1
            previous = nums[i]
        return len(nums) - 1

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        idx = self.find_start_index(nums)
        result = [nums[idx] ** 2]
        left_idx, right_idx = idx - 1, idx + 1

        while left_idx >= 0 and right_idx < n:
            left = nums[left_idx] ** 2
            right = nums[right_idx] ** 2
            if left <= right:
                result.append(left)
                left_idx -= 1
            else:
                result.append(right)
                right_idx += 1

        if left_idx >= 0:
            for i in range(left_idx, -1, -1):
                result.append(nums[i] ** 2)
        if right_idx < n:
            for i in range(right_idx, n):
                result.append(nums[i] ** 2)
        return result