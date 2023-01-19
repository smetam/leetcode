import pytest
from power_of_two import Solution


@pytest.mark.parametrize('nums, expected', [
    (1, True),
    (16, True),
    (3, False),
    (-8, False),
])
def test_solution(nums, expected):
    assert Solution().isPowerOfTwo(nums) == expected
