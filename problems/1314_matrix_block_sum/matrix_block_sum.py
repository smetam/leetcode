from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n_rows, n_cols = len(mat), len(mat[0])
        dp = [[0 for _ in range(n_cols + 1)] for _ in range(n_rows + 1)]
        for row_idx in range(n_rows):
            row = mat[row_idx]
            col_sum = 0
            for col_idx in range(n_cols):
                val = row[col_idx]
                col_sum += val
                dp[row_idx+1][col_idx+1] = dp[row_idx][col_idx+1] + col_sum
        
        for row_idx in range(n_rows):
            for col_idx in range(n_cols):
                max_row, max_col = min(row_idx + k + 1, n_rows), min(col_idx + k + 1, n_cols)
                min_row, min_col = max(row_idx - k, 0), max(col_idx - k, 0)
                
                mat[row_idx][col_idx] = (
                    dp[max_row][max_col] 
                    + dp[min_row][min_col] 
                    - dp[max_row][min_col]
                    - dp[min_row][max_col]
                )
        return mat
