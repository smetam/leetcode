import pytest
from triangle import Solution


@pytest.mark.parametrize('triangle, expected', [
    ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
    ([[-10]], -10),
])
def test_solution(triangle, expected):
    assert Solution().minimumTotal(triangle) == expected
