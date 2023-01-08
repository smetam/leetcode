class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        return sum(map(int, n[2:]))