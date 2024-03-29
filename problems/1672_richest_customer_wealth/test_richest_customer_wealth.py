import pytest
from richest_customer_wealth import Solution


@pytest.mark.parametrize('accounts, expected', [
    ([[1,2,3],[3,2,1]], 6),
    ([[1,5],[7,3],[3,5]], 10),
    ([[2,8,7],[7,1,3],[1,9,5]], 17),
])
def test_solution(accounts, expected):
    assert Solution().maximumWealth(accounts) == expected
