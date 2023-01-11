import pytest
from check_if_one_string_swap_can_make_strings_equal import Solution


@pytest.mark.parametrize('s1, s2, expected', [
    ("bank", "kanb", True),
    ("attack", "defend", False),
    ("kelb", "kelb", True),
    ("qgqeg", "gqgeq", False)
])
def test_solution(s1, s2, expected):
    assert Solution().areAlmostEqual(s1, s2) == expected
