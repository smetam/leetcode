from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n_rows, n_cols = len(grid2), len(grid2[0])
        visited = set()

        def is_sub_island(r: int, c: int) -> bool:
            visited.add((r, c))
            is_sub = grid1[r][c] == 1
            
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                # skip if outside of grid
                if any([nr < 0, nr >= n_rows, nc < 0, nc >= n_cols]):
                    continue

                # skip if it is water
                if grid2[nr][nc] == 0:
                    continue

                # skip if already visited
                if (nr, nc) in visited:
                    continue
                
                is_sub = is_sub_island(nr, nc) and is_sub
            return is_sub

        total_sub_islands = 0
        for row in range(n_rows):
            for col in range(n_cols):
                # skip if it is water
                if grid2[row][col] == 0:
                    continue

                # skip if already visited
                if (row, col) in visited:
                    continue
                
                if is_sub_island(row, col):
                    total_sub_islands += 1
        return total_sub_islands
