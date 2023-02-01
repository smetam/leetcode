from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n_rows, n_cols = len(maze), len(maze[0])
        row, col = entrance

        visited = set()
        visited.add((row, col))
        q = deque()
        q.append((row, col, 0))
        while len(q) > 0:
            r, c, steps = q.popleft()
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                # if it is outside the maze
                if nr < 0 or nc < 0 or nr >= n_rows or nc >= n_cols:
                    continue
                
                if (nr, nc) in visited:
                    continue

                is_wall = maze[nr][nc] == '+'
                if is_wall:
                    continue

                # if it is at the border of maze - we found an exit
                if nr == 0 or nc == 0 or nr == n_rows - 1 or nc == n_cols - 1:
                    return steps + 1

                visited.add((nr, nc))
                q.append((nr,nc,steps+1))

        return -1