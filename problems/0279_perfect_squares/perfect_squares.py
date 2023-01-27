class Solution:
    def numSquares(self, n: int) -> int:
        def is_perfect_square(m: int) -> bool:
            s = int(m ** 0.5)
            return s * s == m

        if is_perfect_square(n):
            return 1

        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            if is_perfect_square(i):
                dp[i] = 1
            else:
                
                min_squares = i
                for j in range(int(i ** 0.5), 1, -1):
                    squared = j ** 2
                    squares = 1 + dp[i-squared]
                    min_squares = min(min_squares, squares)
                dp[i] = min_squares
        
        return dp[-1]


# O(n^2)
class Solution1:
    def numSquares(self, n: int) -> int:

        def is_perfect_square(m: int) -> bool:
            s = int(m ** 0.5)
            return s * s == m

        if is_perfect_square(n):
            return 1

        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            if is_perfect_square(i):
                dp[i] = 1
            else:
                min_squares = i
                for j in range(1, i):
                    squares = dp[j] + dp[i-j]
                    min_squares = min(min_squares, squares)
                dp[i] = min_squares
        return dp[-1]