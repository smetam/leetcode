class Solution:
    def tribonacci(self, n: int) -> int:
        previous, current, next = 0, 0, 1
        for _ in range(n):
            previous, current, next = current, next, previous + current + next
        return current