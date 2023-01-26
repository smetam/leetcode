from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        signs = []
        for prev, curr in zip(nums[:-1], nums[1:]):
            new_sign = curr - prev
            if new_sign != 0:
                new_sign = new_sign // abs(new_sign)
                signs.append(new_sign)

        res = len(signs) + 1
        for prev, curr in zip(signs[:-1], signs[1:]):
            if prev == curr:
                res -= 1
        return res

