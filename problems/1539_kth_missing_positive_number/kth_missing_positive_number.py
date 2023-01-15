from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        max_num = arr[-1]
        if max_num == n:
            # this means there are no gaps in arr
            return n + k
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            n_missing = arr[mid] - mid - 1
            if k <= n_missing:
                right = mid - 1
            else: 
                left = mid + 1
        return k + right + 1
