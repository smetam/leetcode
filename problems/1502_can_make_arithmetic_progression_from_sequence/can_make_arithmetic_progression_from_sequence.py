from typing import List
import heapq


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        heapq.heapify(arr)
        curr, nxt = heapq.heappop(arr), heapq.heappop(arr)
        diff = curr - nxt
        while len(arr) > 0:
            curr, nxt = nxt, heapq.heappop(arr)
            if diff != curr - nxt:
                return False
        return True