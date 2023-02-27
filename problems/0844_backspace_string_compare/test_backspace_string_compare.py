import pytest
from backspace_string_compare import Solution


@pytest.mark.parametrize('s, t, expected', [
    ("ab#c", "ad#c", True),
    ("ab##", "c#d#", True),
    ("a#c", "b", False),
])
def test_solution(s, t, expected):
    assert Solution().backspaceCompare(s, t) == expected
