import pytest
from is_subsequence import Solution


@pytest.mark.parametrize('s, t, expected', [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("", "ahbgdc", True),
])
def test_solution(s, t, expected):
    assert Solution().isSubsequence(s, t) == expected
