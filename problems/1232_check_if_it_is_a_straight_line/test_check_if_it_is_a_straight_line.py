import pytest
from check_if_it_is_a_straight_line import Solution


@pytest.mark.parametrize('coordinates, expected', [
    ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], True),
    ([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]], False),
    ([[1,2],[1,3],[1,4],[1,5],[1,6]], True),
    ([[2,2],[3,2],[4,2],[5,2],[6,2]], True),
    ([[1,2],[1,3],[1,4],[1,5],[1,6],[6,7]], False),
])
def test_solution(coordinates, expected):
    assert Solution().checkStraightLine(coordinates) == expected
