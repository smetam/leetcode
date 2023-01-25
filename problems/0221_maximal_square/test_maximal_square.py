import pytest
from maximal_square import Solution


@pytest.mark.parametrize('matrix, expected', [
    ([
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ], 4),
    ([
        ["0","1"],
        ["1","0"]
    ], 1),
    ([[0]], 0),
])
def test_solution(matrix, expected):
    assert Solution().maximalSquare(matrix) == expected
