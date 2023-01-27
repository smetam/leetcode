class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3: 
            return 2
        div, mod = (n - 2) // 3, (n - 2) % 3 + 2
        return 3 ** div * mod


class Solution1:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        for i in range(n + 1):
            max_prod = 1
            for j in range(i//2, i):
                prod = max(dp[j], j) * max(dp[i-j], i-j)
                max_prod = max(max_prod, prod)
            dp[i] = max_prod 
        return dp[-1] 