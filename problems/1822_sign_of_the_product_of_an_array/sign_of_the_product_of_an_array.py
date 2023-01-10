from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n_negative = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                n_negative += 1

        return -1 if n_negative % 2 == 1 else 1