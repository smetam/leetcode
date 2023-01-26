class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]
        for i in range(len1 + 1):
            dp[0][i] = i
        for i in range(len2 + 1):
            dp[i][0] = i
        for row in range(1, len2 + 1):
            for col in range(1, len1 + 1):
                sym1 = word1[col-1]
                sym2 = word2[row-1]
                if sym1 == sym2:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] = 1 + min(
                        dp[row-1][col-1],
                        dp[row-1][col],
                        dp[row][col-1]
                    )
        return dp[-1][-1]

