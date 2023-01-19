
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == x ** 2:
        #       bin(n) == 0b1000...
        # and bin(n-1) == 0b0111...
        # so (n & n - 1) == 0
        return n > 0 and not (n & n - 1)


class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return sum(map(int, bin(n)[2:])) == 1