import pytest
from zigzag_conversion import Solution

@pytest.mark.parametrize('s, num_rows, expected_result', [
    ['PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'],
    ['PAYPALISHIRING', 4, 'PINALSIGYAHRPI'],
    ['A', 1, "A"],
    ['AB', 1, "AB"],
])
def test_solution(s, num_rows, expected_result):
    assert Solution().convert(s, numRows=num_rows) == expected_result
