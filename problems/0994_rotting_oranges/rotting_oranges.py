from typing import List


class Solution:
    @staticmethod
    def is_on_grid(r: int, c: int, m: int, n: int) -> bool:
            return (0 <= r < m) and (0 <= c < n)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = set()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh.add((row, col))

        minutes = 0
        updated = True
        while updated:
            updated = False
            to_rot = set()
            for row, col in fresh:
                neighbours = ((row+1, col), (row-1, col), (row, col+1), (row, col-1))
                neighbours = [grid[r][c] for r, c in neighbours if self.is_on_grid(r,c,m,n)]
                if any(neighbour == 2 for neighbour in neighbours):
                    to_rot.add((row, col))

            if len(to_rot) > 0:
                updated = True
                minutes += 1
                for row, col in to_rot:
                    grid[row][col] = 2
                    fresh.remove((row, col))

        return -1 if len(fresh) > 0 else minutes

