import pytest
from reshape_the_matrix import Solution


@pytest.mark.parametrize('mat, r, c, expected', [
    ([[1,2],[3,4]], 1, 4, [[1,2,3,4]]),
    ([[1,2],[3,4]], 2, 4, [[1,2],[3,4]]),
])
def test_solution(mat, r, c, expected):
    assert Solution().matrixReshape(mat, r, c) == expected
