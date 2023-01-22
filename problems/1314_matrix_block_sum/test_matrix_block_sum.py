import pytest
from matrix_block_sum import Solution


@pytest.mark.parametrize('mat, k, expected', [
    ([
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ], 1, [
        [12,21,16],
        [27,45,33],
        [24,39,28],
    ]),
    ([
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ], 2, [
        [45,45,45],
        [45,45,45],
        [45,45,45],
    ]),
])
def test_solution(mat, k, expected):
    assert Solution().matrixBlockSum(mat, k) == expected
