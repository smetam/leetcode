from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        visited = set()

        def count_boundary(r, c):
            is_boundary = False
            visited.add((r,c))
            total_size = 1

            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if any([nr < 0, nr >= n_rows, nc < 0, nc >= n_cols]):
                    is_boundary = True
                    continue

                if (nr, nc) in visited:
                    continue

                if grid[nr][nc] == 0:
                    continue

                size, is_bndry = count_boundary(nr, nc)
                total_size += size
                is_boundary = is_boundary or is_bndry
            return total_size, is_boundary

        total_size = 0
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 0:
                    continue

                if (row, col) in visited:
                    continue

                size, is_bndry = count_boundary(row, col)
                if not is_bndry:
                    total_size += size
        return total_size
