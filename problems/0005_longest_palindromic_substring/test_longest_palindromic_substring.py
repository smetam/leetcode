import pytest
from longest_palindromic_substring import Solution


@pytest.mark.parametrize('s, expected', [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("cbbc", "cbbc"),
    ("bbbc", "bbb"),
])
def test_solution(s, expected):
    assert Solution().longestPalindrome(s) == expected
