from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        height_left = [0 for _ in range(n)]
        height_right = [0 for _ in range(n)]
        max_left, max_right = 0, 0
        for idx in range(n):
            max_left = max(max_left, height[idx])
            height_left[idx] = max_left

            max_right = max(max_right, height[n-1-idx])
            height_right[n-1-idx] = max_right
        
        trapped_volume = 0
        for left, right, h in zip(height_left, height_right, height):
            trapped_volume += min(left, right) - h
        return trapped_volume
        
