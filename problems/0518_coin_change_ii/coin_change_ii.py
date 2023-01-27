from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[1] + [0 for _ in range(amount)] for _ in range(len(coins))]
        for idx, coin in enumerate(coins):
            for am in range(1, amount + 1):
                with_coin = dp[idx][am-coin] if am-coin >= 0 else 0
                withount_coin = dp[idx-1][am] 
                dp[idx][am] = with_coin + withount_coin
        return dp[-1][-1]