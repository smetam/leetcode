import pytest
from kth_missing_positive_number import Solution


@pytest.mark.parametrize('arr, k, expected', [
    ([2,3,4,7,11], 5, 9),
    ([2,3,4,7,11], 6, 10),
    ([2,3,4,7,11], 1, 1),
    ([1,2,3,4], 2, 6),
    ([1,2,3,4], 3, 7),
    ([1,3], 1, 2),
    ([1,10,21,22,25], 12, 14),
])
def test_solution(arr, k, expected):
    assert Solution().findKthPositive(arr, k) == expected
