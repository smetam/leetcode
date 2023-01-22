class Solution:
    def numTrees(self, n: int) -> int:
        # for zero nodes there is only one way
        dp = [1]
        for k in range(1, n + 1):
            num_trees = 0
            # we can choose any number to be root node
            for i in range(1, k + 1):
                # after that we divide all numbers in to < k and > k
                num_trees += dp[i-1] * dp[k-i]
            dp.append(num_trees)
        return dp[-1]