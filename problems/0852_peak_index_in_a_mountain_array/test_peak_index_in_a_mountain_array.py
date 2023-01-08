import pytest
from peak_index_in_a_mountain_array import Solution


@pytest.mark.parametrize('arr, expected', [
    ([0,1,0], 1),
    ([0,2,1,0], 1),
    ([0,10,5,2], 1),
])
def test_solution(arr, expected):
    assert Solution().peakIndexInMountainArray(arr) == expected
