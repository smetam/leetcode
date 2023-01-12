from typing import List


class Solution:

    @staticmethod
    def search(arr: List[int], target: int) -> int:
        left, right = 0, len(arr) 
        while left + 1 != right:
            mid = (left + right) // 2
            if target < arr[mid]:
                right = mid
            else:
                left = mid
        return left

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_col = [row[0] for row in matrix]
        row_idx = self.search(first_col, target)
        row = matrix[row_idx]
        col_idx = self.search(row, target)
        return row[col_idx] == target
