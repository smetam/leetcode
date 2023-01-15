from itertools import count


# Direct calculation approach
class Solution:

    def arrangeCoins(self, n: int) -> int:
        return int((2 * n + 0.25) ** 0.5 - 0.5)


# Binsearch approach
class Solution1:

    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2
            if n < coins:
                right = mid - 1
            else:
                left = mid + 1
        return right


#  Straightforward approach
class Solution2:

    def arrangeCoins(self, n: int) -> int:
        total = 0
        for i in count(1):
            total += i
            if total > n:
                return i - 1