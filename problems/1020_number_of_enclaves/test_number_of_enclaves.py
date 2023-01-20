import pytest
from number_of_enclaves import Solution


@pytest.mark.parametrize('grid, expected', [
    ([
        [0,0,0,0],
        [1,0,1,0],
        [0,1,1,0],
        [0,0,0,0],
    ], 3),
    ([
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,0],
        [0,0,0,0],
    ], 0),
])
def test_solution(grid, expected):
    assert Solution().numEnclaves(grid) == expected
