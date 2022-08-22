class Solution:

    def get_next_row_and_delta(self, current_row: int, num_rows: int, delta: int) -> int:
        if (num_rows == 1) or (delta == 0):
            return 0, 0
        if current_row == 0:
            return 1, 1
        if current_row == num_rows - 1:
            return current_row - 1, -1
        return current_row + delta, delta

    def convert(self, s: str, numRows: int) -> str:
        rows = {i: '' for i in range(numRows)}
        current_row = 0
        delta = 1
        for i, symbol in enumerate(s):
            rows[current_row] += symbol
            delta
            current_row, delta = self.get_next_row_and_delta(current_row, numRows, delta)
        result = ''
        for i in range(numRows):
            result += rows[i]
        return result



class Solution2:

    def convert(self, s: str, numRows: int) -> str:
        result = s[0]
        current_row = 0
        current_pos = 0
        for i in range(1, len(s)):
            next_pos = 


