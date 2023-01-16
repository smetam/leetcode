from typing import List
import heapq


class Solution:
    @staticmethod
    def number_of_soldiers(arr: list) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == 0:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for idx, row in enumerate(mat):
            n_soldiers = self.number_of_soldiers(row)
            heapq.heappush(heap, (n_soldiers, idx))
        res = [heapq.heappop(heap)[1] for _ in range(k)]
        return res
        

