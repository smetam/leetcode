from typing import List
from itertools import chain


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        result = [[0 for _ in range(c)] for _ in range(r)]
        for i, val in enumerate(chain.from_iterable(mat)):
            print(val)
            row = i // c
            col = i % c
            result[row][col] = val
        return result
