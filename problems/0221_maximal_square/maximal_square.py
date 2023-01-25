from typing import List
from itertools import chain


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n_rows, n_cols = len(matrix), len(matrix[0])
        for row in range(n_rows):
            for col in range(n_cols):
                val = matrix[row][col]
                if row == 0 or col == 0:
                    matrix[row][col] = int(val)
                    continue
                if val == '0':
                    matrix[row][col] = 0
                    continue
                matrix[row][col] = 1 + min(
                    matrix[row-1][col],
                    matrix[row-1][col-1],
                    matrix[row][col-1],
                )

        max_side = max(chain.from_iterable(matrix))
        return max_side ** 2
        
        