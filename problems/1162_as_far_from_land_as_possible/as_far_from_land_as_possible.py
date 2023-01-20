from typing import List
from itertools import chain


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        distances = [[n_rows+n_cols for _ in range(n_cols)] for _ in range(n_rows)]

        def update(row, col, dist):
            if row < 0 or col < 0:
                return
            current = distances[row][col]
            if current > dist:
                distances[row][col] = dist
                update(row-1, col, dist+1)
                update(row, col-1, dist+1)

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1:
                    new_dist = 0
                if grid[row][col] == 0:
                    new_dist = 1 + min(distances[row-1][col], distances[row][col-1])
                update(row, col, new_dist)

        max_dist = max(chain.from_iterable(distances))
        if max_dist in (0, n_rows+n_cols):
            return -1
        return max_dist