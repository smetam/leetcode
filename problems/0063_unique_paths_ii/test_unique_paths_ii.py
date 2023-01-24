import pytest
from unique_paths_ii import Solution


@pytest.mark.parametrize('obstacleGrid, expected', [
    ([[0,0,0],[0,1,0],[0,0,0]], 2),
    ([[0,1],[0,0]], 1),
])
def test_solution(obstacleGrid, expected):
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == expected
