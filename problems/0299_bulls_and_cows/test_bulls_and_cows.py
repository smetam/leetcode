import pytest
from bulls_and_cows import Solution


@pytest.mark.parametrize('secret, guess, expected', [
    ("1807", "7810", "1A3B"),
    ("1123", "0111", "1A1B"),
])
def test_solution(secret, guess, expected):
    assert Solution().getHint(secret, guess) == expected
