import pytest
from maximum_subarray import Solution

@pytest.mark.parametrize('nums, expected_result', [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([5,4,-1,7,8], 23),
])
def test_solution(nums, expected_result):
    assert Solution().maxSubArray(nums) == expected_result
