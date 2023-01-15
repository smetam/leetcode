import pytest
from decrypt_string_from_alphabet_to_integer_mapping import Solution


@pytest.mark.parametrize('s, expected', [
    ("10#11#12", "jkab"),
    ("1326#", "acz"),
])
def test_solution(s, expected):
    assert Solution().freqAlphabets(s) == expected
