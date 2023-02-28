import pytest
from last_stone_weight import Solution


@pytest.mark.parametrize('stones, expected', [
    ([2,7,4,1,8,1], 1),
    ([1], 1),
])
def test_solution(stones, expected):
    assert Solution().lastStoneWeight(stones) == expected
