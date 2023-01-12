class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            squared = mid ** 2
            if squared == num:
                return True
            if squared < num:
                left = mid + 1
            else:
                right = mid - 1
        return False