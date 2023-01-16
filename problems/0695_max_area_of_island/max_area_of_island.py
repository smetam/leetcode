from typing import List
import heapq


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])

        def is_on_grid(coord: tuple) -> bool:
            r, c = coord
            return (0 <= r < n_rows) and (0 <= c < n_cols) 

        visited = set()
        heap = [0]

        for row in range(n_rows):
            for col in range(n_cols):
                if (row, col) in visited:
                    continue
                is_island = grid[row][col] == 1
                if not is_island:
                    continue
                q = [(row, col)]
                visited.add((row,col))
                island_size = 0
                while len(q) > 0:
                    r, c = q.pop()
                    island_size += 1
                    for coord in ((r + 1, c), (r-1, c), (r, c+1), (r, c-1)):
                        if (
                            is_on_grid(coord) 
                            and (coord not in visited)
                            and grid[coord[0]][coord[1]] == 1
                        ):  
                            visited.add(coord)
                            q.append(coord)
                heapq.heappush(heap, -island_size)
        return -heap[0]

