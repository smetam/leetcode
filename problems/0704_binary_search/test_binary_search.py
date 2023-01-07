import pytest
from binary_search import Solution

@pytest.mark.parametrize('nums, target, expected_result', [
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12], 2, -1),
    ([-1,0,5], -1, 0),
])
def test_solution(nums, target, expected_result):
    assert Solution().search(nums, target) == expected_result
