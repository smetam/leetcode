import pytest
from minimum_falling_path_sum import Solution


@pytest.mark.parametrize('matrix, expected', [
    ([[2,1,3],[6,5,4],[7,8,9]], 13),
    ([[-19,57],[-40,-5]], -59),
])
def test_solution(matrix, expected):
    assert Solution().minFallingPathSum(matrix) == expected
