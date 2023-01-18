from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = max(nums)
        cumprod_positive = 1
        cumprod_negative = 1
        for num in nums:
            if num == 0:
                cumprod_positive, cumprod_negative = 0, 0
            elif num > 0:
                cumprod_positive, cumprod_negative = max(cumprod_positive, 1) * num, cumprod_negative * num
            else:
                cumprod_positive, cumprod_negative = cumprod_negative * num, max(cumprod_positive, 1) * num
            maxprod = max(maxprod, cumprod_positive)
        return maxprod