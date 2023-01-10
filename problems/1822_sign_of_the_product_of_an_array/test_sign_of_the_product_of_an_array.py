import pytest
from sign_of_the_product_of_an_array import Solution


@pytest.mark.parametrize('nums, expected', [
    ([-1,-2,-3,-4,3,2,1], 1),
    ([1,5,0,2,-3], 0),
    ([-1,1,-1,1,-1], -1),
])
def test_solution(nums, expected):
    assert Solution().arraySign(nums) == expected
