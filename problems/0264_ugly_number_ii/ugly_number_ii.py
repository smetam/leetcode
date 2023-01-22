# 7, 11, 13, 14, 17, 19, 21, 22, 23, 
# 1
# 2
# 3
# 2^2 = 4
# 5
# 3 * 2 = 6
# 2^3 = 8
# 2*5 = 10
# 2^2 * 3 = 12
# 2*5 = 15
# 2^4 = 16
# 2 * 3^2 = 18
# 2^2 * 5 = 20
# 2^3 * 3 = 24
# 5^2 = 25

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = (2, 3, 5)
        k = len(factors)
        ugly_numbers = [1] 
        pointers = [0 for _ in range(k)]
        for _ in range(n-1):
            candidates = [factor * ugly_numbers[p] for factor, p in zip(factors, pointers)]
            next_ugly_number = min(candidates)
            ugly_numbers.append(next_ugly_number)
            pointers = [p + int(candidate == next_ugly_number) for candidate, p in zip(candidates, pointers)]
        return ugly_numbers[-1]


# this does takes too much time since ugly numbers become very sparse eventually
class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        dp = [True]
        num = 1 
        i = 1
        while i < n:
            num += 1
            is_ugly = False
            for div in (2, 3, 5):
                rem, mod = num // div, num % div
                if mod == 0:
                    is_ugly = dp[rem - 1]
                    break
            dp.append(is_ugly)
            if is_ugly:
                i += 1
        return num