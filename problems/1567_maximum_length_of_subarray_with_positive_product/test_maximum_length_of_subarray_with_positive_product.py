import pytest
from maximum_length_of_subarray_with_positive_product import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,-2,-3,4], 4),
    ([0,1,-2,-3,-4], 3),
    ([-1,-2,-3,0,1], 2),
    ([-1], 0),
    ([-1,-1], 2),
    ([1,-1], 1),
    ([1,2,3,5,-6,4,0,10], 4)
])
def test_solution(nums, expected):
    assert Solution().getMaxLen(nums) == expected
