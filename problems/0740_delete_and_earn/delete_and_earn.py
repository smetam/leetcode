from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        left = min(c)
        right = max(c)
        prev, curr = 0, c[left] * left
        for i in range(left + 1, right + 1):
            prev, curr = curr, max(curr, prev + c[i] * i)
        return curr

