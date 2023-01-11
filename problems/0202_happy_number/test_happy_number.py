import pytest
from happy_number import Solution


@pytest.mark.parametrize('nums, expected', [
    (19, True),
    (2, False),
])
def test_solution(nums, expected):
    assert Solution().isHappy(nums) == expected
