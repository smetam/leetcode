import pytest
from valid_parentheses import Solution


@pytest.mark.parametrize('s, expected', [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("(([]({})))", True),
    ("(([]){})))", False),
])
def test_solution(s, expected):
    assert Solution().isValid(s) == expected
