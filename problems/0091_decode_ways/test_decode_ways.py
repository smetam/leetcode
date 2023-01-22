import pytest
from decode_ways import Solution


@pytest.mark.parametrize('s, expected', [
    ('12', 2),
    ("226", 3),
    ('06', 0),
    ('106', 1),
])
def test_solution(s, expected):
    assert Solution().numDecodings(s) == expected
