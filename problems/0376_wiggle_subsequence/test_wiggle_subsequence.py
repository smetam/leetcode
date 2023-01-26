import pytest
from wiggle_subsequence import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,7,4,9,2,5], 6),
    ([1,17,5,10,13,15,10,5,16,8], 7),
    ([1,2,3,4,5,6,7,8,9], 2),
    ([5], 1),
])
def test_solution(nums, expected):
    assert Solution().wiggleMaxLength(nums) == expected
