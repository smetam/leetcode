import pytest
from ransom_note import Solution


@pytest.mark.parametrize('ransomNote, magazine, expected', [
    ('a', 'b', False),
    ('aa', 'ab', False),
    ('aa', 'aab', True),
])
def test_solution(ransomNote, magazine, expected):
    assert Solution().canConstruct(ransomNote, magazine) == expected
