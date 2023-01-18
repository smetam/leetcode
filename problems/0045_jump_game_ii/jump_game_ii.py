from typing import List


class Solution:

    # O(n)
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        jumps = 0
        while right < n - 1:
            jumps += 1
            left, right = right + 1, max(i + nums[i] for i in range(left, right + 1))
        return jumps

class Solution1:

    # can be O(n^2) in worst case
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        min_jumps = [n for _ in range(n)]
        min_jumps[0] = 0
        for jump_start_pos, num in enumerate(nums):
            max_jump_pos = min(jump_start_pos + num + 1, n)
            for jump_end_pos in range(jump_start_pos + 1, max_jump_pos):
                min_jumps[jump_end_pos] = min(min_jumps[jump_end_pos], min_jumps[jump_start_pos] + 1)

        return min_jumps[-1]

