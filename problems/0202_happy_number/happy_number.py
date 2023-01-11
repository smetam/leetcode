class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = sum(map(lambda x: int(x) ** 2, str(n)))
        return False
