import pytest
from search_in_rotated_sorted_array import Solution


@pytest.mark.parametrize('nums, target, expected', [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([4,5,6,1,2], 3, -1),
    ([4,5,6,1,2], 4, 0),
    ([4,5,6,1,2], 5, 1),
    ([4,5,6,1,2], 6, 2),
    ([4,5,6,1,2], 1, 3),
    ([4,5,6,1,2], 2, 4),
    ([1,3], 1, 0),
    ([3,1], 1, 1),
    ([1], 0, -1),
])
def test_solution(nums, target, expected):
    assert Solution().search(nums, target) == expected
