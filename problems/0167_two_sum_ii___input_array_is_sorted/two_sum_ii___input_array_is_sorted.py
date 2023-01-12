from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers)
        while left + 1 != right:
            current_sum = numbers[left - 1] + numbers[right - 1]
            if current_sum == target:
                return left, right
            if current_sum < target:
                left += 1
            else: 
                right -= 1
        return left, right
            

