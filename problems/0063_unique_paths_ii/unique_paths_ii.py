from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n_rows, n_cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        for row in range(n_rows):
            if obstacleGrid[row][0] != 1:
                dp[row][0] = 1
            else:
                break
        for col in range(n_cols):
            if obstacleGrid[0][col] != 1:
                dp[0][col] = 1
            else: break

        for row in range(1, n_rows):
            for col in range(1, n_cols):
                is_obstacle = obstacleGrid[row][col]
                if is_obstacle:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[-1][-1]