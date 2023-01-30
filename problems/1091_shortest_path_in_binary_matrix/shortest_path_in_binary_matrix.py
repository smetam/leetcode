from typing import List
from collections import deque

# O(n^2) memory, O(n^2) time 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        q = deque()
        visited = set()

        visited.add((0,0))
        q.append((0,0,1))

        def update(r: int, c: int, val: int):
            # check if (r,c) is within grid limits
            if r < 0 or r >=n or c < 0 or c >= n:
                return -1
            
            # check if it is an obstacle
            is_obstacle = grid[r][c]
            if is_obstacle:
                return -1
            
            for nr, nc in (
                (r-1, c-1), 
                (r-1, c), 
                (r-1, c+1), 
                (r, c-1), 
                (r, c+1), 
                (r+1, c-1), 
                (r+1, c), 
                (r+1, c+1), 
            ):  
                if (nr, nc) not in visited:
                    q.append((nr, nc, val+1))
                    visited.add((nr, nc))
            return val

        while len(q) > 0:
            r, c, val = q.popleft()
            res = update(r, c, val)
            if (r, c) == (n-1, n-1):
                return res
            
        return -1
