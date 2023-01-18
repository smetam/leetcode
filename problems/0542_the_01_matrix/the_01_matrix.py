from typing import List


class Solution:
    @classmethod
    def update(cls, res, row, col, new_val):
        if row < 0 or col < 0:
            return
        val = res[row][col]
        if new_val >= val:
            return
        res[row][col] = new_val
        cls.update(res, row-1, col, new_val+1)
        cls.update(res, row, col-1, new_val+1)

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        fill_vall = max(n, m)
        res = [[fill_vall for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                val = mat[row][col]
                if val == 0:
                    new_val = 0
                else:
                    new_val = fill_vall
                    for r, c in ((row - 1, col), (row, col - 1)):
                        if r >=0 and c >= 0:
                            new_val = min(new_val, res[r][c] + 1)
                self.update(res, row, col, new_val)
        return res
