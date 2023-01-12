from typing import List


class Solution:
    @staticmethod
    def is_within_distance(target: int, arr: List[int], d: int) -> bool:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            num = arr[mid]
            if target - d <= num <= target + d:
                return True
            if target < num:
                right = mid - 1
            else: 
                left = mid + 1
        return False
                
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = list(sorted(arr2))
        res = 0
        for num1 in arr1:
            res += int(not self.is_within_distance(num1, arr2, d))
        return res