import pytest
from as_far_from_land_as_possible import Solution


@pytest.mark.parametrize('grid, expected', [
    ([
        [1,0,1],
        [0,0,0],
        [1,0,1],
    ], 2),
    ([
        [1,0,0],
        [0,0,0],
        [0,0,0],
    ], 4),
    ([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], -1),
    ([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], -1),
])
def test_solution(grid, expected):
    assert Solution().maxDistance(grid) == expected
