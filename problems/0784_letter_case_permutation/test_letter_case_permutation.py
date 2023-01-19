import pytest
from letter_case_permutation import Solution


@pytest.mark.parametrize('s, expected', [
    ("a1b2", ["a1b2","a1B2","A1b2","A1B2"]),
    ("3z4", ["3z4","3Z4"]),
])
def test_solution(s, expected):
    assert set(Solution().letterCasePermutation(s)) == set(expected)
