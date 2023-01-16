import pytest
from delete_and_earn import Solution


@pytest.mark.parametrize('nums, expected', [
    ([3,4,2], 6),
    ([2,2,3,3,3,4], 9),
    ([4], 4)
])
def test_solution(nums, expected):
    assert Solution().deleteAndEarn(nums) == expected
