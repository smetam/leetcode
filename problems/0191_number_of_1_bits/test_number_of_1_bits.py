import pytest
from number_of_1_bits import Solution


@pytest.mark.parametrize('n, expected', [
    (0, 0),
    (1, 1),
    (11, 3),
])
def test_solution(n, expected):
    assert Solution().hammingWeight(n) == expected
