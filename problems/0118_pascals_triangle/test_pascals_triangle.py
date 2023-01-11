import pytest
from pascals_triangle import Solution


@pytest.mark.parametrize('numRows, expected', [
    (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    (1, [[1]]),
])
def test_solution(numRows, expected):
    assert Solution().generate(numRows) == expected
