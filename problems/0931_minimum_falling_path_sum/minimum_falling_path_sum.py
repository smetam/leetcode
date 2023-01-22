from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_sum = matrix[0]
        for row in matrix[1:]:
            new_min_sum = []
            for elem, left, bellow, right in zip(row, min_sum[:1] + min_sum[:-1], min_sum, min_sum[1:] + min_sum[-1:]):
                new_elem = min(left, bellow, right) + elem
                new_min_sum.append(new_elem)
            min_sum = new_min_sum
        return min(min_sum)