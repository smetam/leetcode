from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i] + mat[n-1-i][i]
        if n % 2 == 1:
            mid = n // 2
            res -= mat[mid][mid]
        return res
