from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        for row in range(1, n_rows):
            grid[row][0] += grid[row-1][0]
        for col in range(1, n_cols):
            grid[0][col] += grid[0][col-1]

        for row in range(1, n_rows):
            for col in range(1, n_cols):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        return grid[-1][-1]