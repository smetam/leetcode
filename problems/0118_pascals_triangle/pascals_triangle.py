from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = [[1]]
        for _ in range(1, numRows):
            previous_row = pascals_triangle[-1]
            current_row = [sum(pair) for pair in zip(previous_row[1:], previous_row[:-1])]
            current_row = [1] + current_row + [1]
            pascals_triangle.append(current_row)
        return pascals_triangle
