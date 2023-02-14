import pytest
from jump_game_iii import Solution


@pytest.mark.parametrize('arr, start, expected', [
    ([4,2,3,0,3,1,2], 5, True),
    ([4,2,3,0,3,1,2], 0, True),
    ([3,0,2,1,2], 2, False),
])
def test_solution(arr, start, expected):
    assert Solution().canReach(arr, start) == expected
