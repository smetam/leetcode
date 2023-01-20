import pytest
from count_sub_islands import Solution


@pytest.mark.parametrize('grid1, grid2, expected', [
    ([
        [0, 1],
        [0, 1],
    ], [
        [0, 1],
        [1, 0],
    ], 1),
    ([
        [0, 0],
    ], [
        [0, 1],
    ], 0),
    ([
        [1,1,1,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,0,0,0,0],
        [1,1,0,1,1],
    ], [
        [1,1,1,0,0],
        [0,0,1,1,1],
        [0,1,0,0,0],
        [1,0,1,1,0],
        [0,1,0,1,0],
    ], 3),
    ([
        [1,0,1,0,1],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [1,0,1,0,1],
    ], [
        [0,0,0,0,0],
        [1,1,1,1,1],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [1,0,0,0,1],
    ], 2),
])
def test_solution(grid1, grid2, expected):
    assert Solution().countSubIslands(grid1, grid2) == expected
