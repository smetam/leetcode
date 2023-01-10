import pytest
from largest_perimeter_triangle import Solution


@pytest.mark.parametrize('nums, expected', [
    ([2,1,2], 5),
    ([1,2,1,10], 0),
    ([3,2,3,4], 10),
])
def test_solution(nums, expected):
    assert Solution().largestPerimeter(nums) == expected
