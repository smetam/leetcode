import pytest
from product_and_sum_of_digits import Solution


@pytest.mark.parametrize('n, expected', [
    (234, 15),
    (4421, 21),
])
def test_solution(n, expected):
    assert Solution().subtractProductAndSum(n) == expected
