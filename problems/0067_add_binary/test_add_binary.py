import pytest
from add_binary import Solution


@pytest.mark.parametrize('a, b, expected', [
    ("11", "1", "100"),
    ("1010", "1011", "10101"),
])
def test_solution(a, b, expected):
    assert Solution().addBinary(a, b) == expected
