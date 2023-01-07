from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        n_islands = 0
        visited = set()

        def is_on_grid(r: int, c: int) -> bool:
            return (0 <= r < n_rows) and (0 <= c < n_cols)

        for row in range(n_rows):
            for col in range(n_cols):
                if (row, col) in visited:
                    continue
                value = grid[row][col]
                if value == '0':
                    continue
                n_islands += 1
                to_visit = [(row, col)]
                while len(to_visit) > 0:
                    r, c = to_visit.pop()
                    visited.add((r, c))
                    for neigbour_row, neigbour_col in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if (
                            is_on_grid(neigbour_row, neigbour_col) 
                            and ((neigbour_row, neigbour_col) not in visited) 
                            and (grid[neigbour_row][neigbour_col] != '0')
                        ):
                            to_visit.append((neigbour_row, neigbour_col))

        return n_islands