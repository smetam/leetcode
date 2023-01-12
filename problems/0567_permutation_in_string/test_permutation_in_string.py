import pytest
from permutation_in_string import Solution


@pytest.mark.parametrize('s1, s2, expected', [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),
    ("adc", "dcda", True),
])
def test_solution(s1, s2, expected):
    assert Solution().checkInclusion(s1, s2) == expected
