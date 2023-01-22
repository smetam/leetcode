import pytest
from pascals_triangle_ii import Solution


@pytest.mark.parametrize('rowIndex, expected', [
    (0, [1]),
    (3, [1,3,3,1]),
])
def test_solution(rowIndex, expected):
    assert Solution().getRow(rowIndex) == expected
