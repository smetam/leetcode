# O(n*m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
        for row in range(1, 1 + len2):
            for col in range(1, 1 + len1):
                sym1 = text1[col-1]
                sym2 = text2[row-1]
                if sym1 == sym2:
                    dp[row][col] = dp[row-1][col-1] + 1
                else: 
                    dp[row][col] = max(
                        dp[row-1][col-1],
                        dp[row][col-1],
                        dp[row-1][col],
                    )
        return dp[-1][-1]