import pytest
from valid_anagram import Solution


@pytest.mark.parametrize('s, t, expected', [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
])
def test_solution(s, t, expected):
    assert Solution().isAnagram(s, t) == expected
