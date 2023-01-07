class Solution:
    def fib(self, n: int) -> int:
        current, next = 0, 1
        for _ in range(n):
            current, next  = next, current + next
        return current