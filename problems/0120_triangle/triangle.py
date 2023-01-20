from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[0]
        for row in triangle[1:]:
            current = []
            for idx, elem in enumerate(row):
                if idx == 0:
                    current.append(prev[0] + elem)
                elif idx == len(row) - 1:
                    current.append(prev[-1] + elem)
                else:
                    current.append(min(prev[idx-1], prev[idx]) + elem)
            prev = current
        return min(prev)

