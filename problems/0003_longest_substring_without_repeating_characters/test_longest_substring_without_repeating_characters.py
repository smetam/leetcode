import pytest
from longest_substring_without_repeating_characters import Solution


@pytest.mark.parametrize('s, expected', [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
])
def test_solution(s, expected):
    assert Solution().lengthOfLongestSubstring(s) == expected
