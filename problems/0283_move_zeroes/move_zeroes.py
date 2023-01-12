from typing import List
from collections import deque


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        q = deque()
        for idx in range(len(nums)):
            num = nums[idx]
            if num == 0:
                q.append(idx)
            else:
                if len(q) > 0:
                    insert_idx = q.popleft()
                    nums[insert_idx], nums[idx] = num, 0
                    q.append(idx)
