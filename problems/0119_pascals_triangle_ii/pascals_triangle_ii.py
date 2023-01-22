from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [1] + [sum(pair) for pair in zip(row[:-1], row[1:])] + [1]
        return row