import pytest
from trapping_rain_water import Solution


@pytest.mark.parametrize('height, expected', [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
    ([1], 0),
    ([1,2], 0),
    ([2,1,2], 1),
])
def test_solution(height, expected):
    assert Solution().trap(height) == expected
