from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        for idx, num in enumerate(arr):
            left, right = idx, n - idx - 1
            odd_left, odd_right = left // 2 + 1, right // 2 + 1
            even_left, even_right = (left + 1) // 2, (right + 1) // 2
            modifier = odd_left * odd_right + even_left * even_right
            total += num * modifier
        return total


class Solution2:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        for idx, num in enumerate(arr):
            left, right = idx, n - idx - 1
            space_from_side = 1 + min(left, right)
            modifier = 0
            for odd in range(1, n + 1, 2):
                modifier += min(space_from_side, odd,  n + 1 - odd)
            total += num * modifier
        return total
