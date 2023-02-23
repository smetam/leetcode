import pytest
from longest_palindrome import Solution


@pytest.mark.parametrize('s, expected', [
    ("abccccdd", 7),
    ("a", 1),
])
def test_solution(s, expected):
    assert Solution().longestPalindrome(s) == expected
