from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # multiply by -1 all elements, since heappop returns min elem instead of max
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if first != second:
                diff = first - second
                heapq.heappush(stones, diff)
        if len(stones) == 1:
            return -heapq.heappop(stones)
        return 0