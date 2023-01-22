import pytest
from ugly_number_ii import Solution


@pytest.mark.parametrize('n, expected', [
    (10, 12),
    (1, 1),
    (443, 506250), 
])
def test_solution(n, expected):
    assert Solution().nthUglyNumber(n) == expected
