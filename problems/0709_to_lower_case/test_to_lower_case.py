import pytest
from to_lower_case import Solution


@pytest.mark.parametrize('s, expected', [
    ("Hello", "hello"),
    ("here", "here"),
    ("LOVELY", "lovely"),
    ("al&phaBET", "al&phabet")
])
def test_solution(s, expected):
    assert Solution().toLowerCase(s) == expected
