from typing import List


class Solution:
    def floodFill(
        self, 
        image: List[List[int]], 
        sr: int, 
        sc: int, 
        color: int
    ) -> List[List[int]]:
        current_color = image[sr][sc]
        if current_color == color:
            return image
        n_rows, n_cols = len(image), len(image[0])

        def is_within_limits_and_color_matches(row: int, col: int) -> bool:
            if (0 <= row < n_rows) and (0 <= col < n_cols):
                c = image[row][col]
                return c == current_color
            return False

        fill_pixels = [(sr, sc)]
        while len(fill_pixels) > 0:
            row, col = fill_pixels.pop()
            image[row][col] = color
            for r, c in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                if is_within_limits_and_color_matches(r, c):
                    fill_pixels.append((r, c))
        return image
        
        
        
