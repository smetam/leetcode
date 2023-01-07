import pytest
from guess_number import Solution

@pytest.mark.parametrize('n, pick', [
    (10, 6),
    (1, 1),
    (2, 1),
    (2, 2),
    (4, 4),
])
def test_solution(n, pick):
    def guess(num: int) -> int:
        if num < pick:
            return 1
        if num > pick:
            return -1
        return 0

    assert Solution().guessNumber(n, guess) == pick
