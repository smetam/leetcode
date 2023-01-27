from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = [0] + [-1 for _ in range(amount)]
        for am in range(1, amount + 1):
            coins_counts = [dp[am - coin] for coin in coins if am - coin >= 0]
            coins_counts = [c for c in coins_counts if c != -1]
            dp[am] = -1 if len(coins_counts) == 0 else min(coins_counts) + 1
        
        return dp[-1]


