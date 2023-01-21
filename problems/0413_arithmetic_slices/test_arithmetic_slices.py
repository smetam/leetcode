import pytest
from arithmetic_slices import Solution


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,4], 3),
    ([1], 0),
])
def test_solution(nums, expected):
    assert Solution().numberOfArithmeticSlices(nums) == expected
