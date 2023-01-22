from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])

        dp = [[0 for _ in range(self.n_cols + 1)] for _ in range(self.n_rows + 1)]
        for row_idx in range(self.n_rows):
            row = matrix[row_idx]
            col_sum = 0
            for col_idx in range(self.n_cols):
                val = row[col_idx]
                col_sum += val
                dp[row_idx+1][col_idx+1] = dp[row_idx][col_idx+1] + col_sum
        self.dp = dp


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        max_row, max_col = row2 + 1, col2 + 1 
        min_row, min_col = row1, col1
        
        return (
            self.dp[max_row][max_col] 
            + self.dp[min_row][min_col] 
            - self.dp[max_row][min_col]
            - self.dp[min_row][max_col]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)