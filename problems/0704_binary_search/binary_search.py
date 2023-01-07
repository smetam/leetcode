from typing import List


class Solution:
    def search(self, nums: List[int], target: int, shift=0) -> int:
        n = len(nums)
        if n < 1:
            return -1
        idx = (n - 1) // 2
        number = nums[idx]
        if number == target:
            return idx + shift

        if nums[idx] < target:
            return self.search(
                nums[idx+1:], 
                target=target, 
                shift=shift + idx + 1,
            )
            
        return self.search(
            nums[:idx], 
            target=target, 
            shift=shift,
        )