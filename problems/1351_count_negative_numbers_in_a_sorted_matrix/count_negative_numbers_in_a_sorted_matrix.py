from typing import List, Optional


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        grid = [[0 for _ in range(n)]] + grid
        row = m
        col = 0
        count = 0
        while col < n:
            while (row >= 0) and (grid[row][col] < 0):
                row -= 1
            count += m - row
            col += 1
        return count
                
        