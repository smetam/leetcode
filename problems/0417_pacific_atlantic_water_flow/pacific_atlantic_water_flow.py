from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_rows, n_cols = len(heights), len(heights[0])
        
        def get_ocean_reachable(q) -> List[List[bool]]:
            reachable = [[False for _ in range(n_cols)] for _ in range(n_rows)]
            visited = set(q)
            while len(q) > 0:
                r, c = q.pop()
                reachable[r][c] = True
                height = heights[r][c]
                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if (
                        (0 <= nr < n_rows) 
                        and (0 <= nc < n_cols) 
                        and (heights[nr][nc] >= height)
                        and ((nr, nc) not in visited)
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return reachable

        pacific = get_ocean_reachable(
            [(r, 0) for r in range(n_rows)] 
            + [(0, c) for c in range(n_cols)]
        )
        atlantic = get_ocean_reachable(
            [(r, n_cols-1) for r in range(n_rows)] 
            + [(n_rows-1, c) for c in range(n_cols)]
        )
        both = []
        for row in range(n_rows):
            for col in range(n_cols):
                if atlantic[row][col] and pacific[row][col]:
                    both.append((row, col))
        return both
