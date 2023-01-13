import pytest
from matrix_diagonal_sum import Solution


@pytest.mark.parametrize('mat, expected', [
    ([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ], 25),
    ([
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]
    ], 8),
    ([[5]], 5),
])
def test_solution(mat, expected):
    assert Solution().diagonalSum(mat) == expected
