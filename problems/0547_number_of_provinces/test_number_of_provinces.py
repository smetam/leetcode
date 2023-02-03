import pytest
from number_of_provinces import Solution


@pytest.mark.parametrize('isConnected, expected', [
    ([
        [1,1,0],
        [1,1,0],
        [0,0,1],
    ], 2),
    ([
        [1,0,0],
        [0,1,0],
        [0,0,1],
    ], 3),
])
def test_solution(isConnected, expected):
    assert Solution().findCircleNum(isConnected) == expected
