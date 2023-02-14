from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()

        def can_reach(pos) -> bool:
            if pos < 0 or pos >= n:
                return False

            jump = arr[pos]
            if jump == 0:
                return True
            
            if pos in visited:
                return False
            
            visited.add(pos)
            return can_reach(pos - jump) or can_reach(pos + jump)
        return can_reach(start)