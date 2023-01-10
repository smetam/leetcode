import pytest
from find_nearest_point import Solution


@pytest.mark.parametrize('x, y, points, expected', [
    (3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]], 2),
    (3, 4, [[3,4]], 0),
    (3, 4, [[2,3]], -1),
])
def test_solution(x, y, points, expected):
    assert Solution().nearestValidPoint(x, y, points) == expected
