from typing import List
from itertools import product
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        indices = list(range(n))
        first_island = (-1,-1)
        for row, col in product(indices, indices):
            if grid[row][col] == 1:
                first_island = (row, col)
                break
        visited = set()
        visited.add(first_island)

        island_q = deque()
        island_q.append(first_island)

        water_q = deque()
        
        while len(island_q) > 0:
            r, c = island_q.popleft()

            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                # if outside of grid
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                # if visited
                if (nr, nc) in visited:
                    continue
                
                visited.add((nr,nc))
                # if water
                if grid[nr][nc] == 0:
                    water_q.append((nr,nc,0))
                    continue
                # if land
                island_q.append((nr,nc))

        while len(water_q) > 0:
            r, c, step = water_q.popleft()

            # if it is land - we found the island
            if grid[r][c] == 1:
                return step

            # if it is water
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                # if outside of grid
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                # if visited
                if (nr, nc) in visited:
                    continue
                visited.add((nr,nc))
                water_q.append((nr,nc,step+1))

        return -1
