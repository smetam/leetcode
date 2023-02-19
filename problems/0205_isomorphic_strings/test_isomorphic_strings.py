import pytest
from isomorphic_strings import Solution


@pytest.mark.parametrize('s, t, expected', [
    ("egg", "add", True),
    ("foo", "bar", False),
    ("paper", "title", True),
    ("badc", "baba", False),
])
def test_solution(s, t, expected):
    assert Solution().isIsomorphic(s, t) == expected
