import pytest
from special_array_with_x_elements_greater_than_or_equal_x import Solution


@pytest.mark.parametrize('nums, expected', [
    ([3,5], 2),
    ([0, 0], -1),
    ([0,4,3,0,4], 3),
    ([3,6,7,7,0], -1)
])
def test_solution(nums, expected):
    assert Solution().specialArray(nums) == expected
