class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i ** 2 <= c:
            target = c - i ** 2
            left, right = 0, c
            while left <= right:
                mid = (left + right) // 2
                squared = mid ** 2
                if target == squared:
                    return True
                if target < squared:
                    right = mid - 1
                else:
                    left = mid + 1
            i += 1
        return False
