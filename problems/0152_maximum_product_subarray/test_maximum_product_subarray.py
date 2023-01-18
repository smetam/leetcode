import pytest
from maximum_product_subarray import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,3,-2,4], 6),
    ([-2,0,-1], 0),
    ([1, 0], 1),
    ([1], 1),
    ([-1], -1),
    ([-4,-3,-2], 12),
])
def test_solution(nums, expected):
    assert Solution().maxProduct(nums) == expected
