import pytest
from can_make_arithmetic_progression_from_sequence import Solution


@pytest.mark.parametrize('nums, expected', [
    ([3,5,1], True),
    ([1,2,4], False),
])
def test_solution(nums, expected):
    assert Solution().canMakeArithmeticProgression(nums) == expected
