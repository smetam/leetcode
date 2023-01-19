import pytest
from permutations import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    ([0,1], [[0,1],[1,0]]),
    ([1], [[1]]),
])
def test_solution(nums, expected):
    assert Solution().permute(nums) == expected
