import pytest
from maximum_distance_between_a_pair_of_values import Solution


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([55,30,5,4,2], [100,20,10,10,5], 2),
    ([2,2,2], [10,10,1], 1),
    ([30,29,19,5], [25,25,25,25,25], 2),
    ([30], [25], 0),
    ([30], [35], 0),
])
def test_solution(nums1, nums2, expected):
    assert Solution().maxDistance(nums1, nums2) == expected
