class Solution:
    
    # solution based on edititing distance with reversed string
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        t = s[::-1]
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for row in range(1, n + 1):
            for col in range(1, n + 1):
                if s[row - 1] == t[col - 1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        
        return dp[-1][-1]
