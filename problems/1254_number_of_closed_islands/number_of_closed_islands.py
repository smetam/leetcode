from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        n_rows, n_cols = len(grid), len(grid[0])
        n_islands = 0

        def is_closed(r, c) -> bool:
            visited.add((r, c))
            result = True
            # check neighbours
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if nr < 0 or nr >= n_rows or nc < 0 or nc >= n_cols:
                    result = False
                    continue
                if (nr, nc) in visited:
                    continue
                if grid[nr][nc] == 1:
                    continue
                if not is_closed(nr, nc):
                    result = False
            return result

        
        for row in range(n_rows):
            for col in range(n_cols):

                # check if it is something we already visited
                if (row, col) in visited:
                    continue

                # check if it is water
                val = grid[row][col]
                if val == 1:
                    continue
                
                if is_closed(row, col):
                    n_islands += 1
        return n_islands
