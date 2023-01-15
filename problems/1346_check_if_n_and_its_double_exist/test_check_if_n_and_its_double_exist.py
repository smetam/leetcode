import pytest
from check_if_n_and_its_double_exist import Solution


@pytest.mark.parametrize('arr, expected', [
    ([10,2,5,3], True),
    ([3,1,7,11], False),
])
def test_solution(arr, expected):
    assert Solution().checkIfExist(arr) == expected
