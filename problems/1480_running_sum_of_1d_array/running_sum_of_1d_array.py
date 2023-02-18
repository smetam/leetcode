from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rolling_sum = 0
        result = []
        for num in nums:
            rolling_sum += num
            result.append(rolling_sum)
        return result