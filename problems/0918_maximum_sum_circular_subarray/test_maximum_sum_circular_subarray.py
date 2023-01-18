import pytest
from maximum_sum_circular_subarray import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,-2,3,-2], 3),
    ([5,-3,5], 10),
    ([-3,-2,-3], -2),
    ([1], 1),
    ([-11], -11),
])
def test_solution(nums, expected):
    assert Solution().maxSubarraySumCircular(nums) == expected
