import pytest
from flood_fill import Solution

@pytest.mark.parametrize('image, sr, sc, color, expected', [
    ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2, [[2,2,2],[2,2,0],[2,0,1]]),
    ([[0,0,0],[0,0,0]], 0, 0, 0, [[0,0,0],[0,0,0]]),
])
def test_solution(image, sr, sc, color, expected):

    assert Solution().floodFill(image, sr, sc, color) == expected
