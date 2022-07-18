from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for idx, num in enumerate(nums):
            complementary = target - num
            if complementary in previous:
                complementary_idx = previous[complementary]
                return complementary_idx, idx
            previous[num] = idx