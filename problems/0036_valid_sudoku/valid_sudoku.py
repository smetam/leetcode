from typing import List
from itertools import chain

class Solution:
    @staticmethod
    def is_valid_element(element: List) -> bool:
        element = [int(item) for item in element if item != '.']
        within_limits = all(map(lambda x: 1 <= x <= 9, element))
        all_unique = len(element) == len(set(element))
        return within_limits and all_unique

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            valid = self.is_valid_element(row)
            if not valid:
                return False

        for col_idx in range(9):
            col = [row[col_idx] for row in board]
            valid = self.is_valid_element(col)
            if not valid:
                return False

        for square_idx in range(9):
            row_idx = (square_idx // 3) * 3
            col_idx = (square_idx % 3) * 3
            square = [row[col_idx: col_idx + 3] for row in board[row_idx: row_idx + 3]]
            valid = self.is_valid_element(chain.from_iterable(square))
            if not valid:
                return False
        return True
