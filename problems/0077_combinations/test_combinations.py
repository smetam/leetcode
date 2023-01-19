import pytest
from combinations import Solution


@pytest.mark.parametrize('n, k, expected', [
    (4, 2, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]),
    (3, 3, [[1,2,3]]),
    (4, 3, [[1,2,3], [1,2,4], [1,3,4], [2,3,4]]),
    (1, 1, [[1]]),
])
def test_solution(n, k, expected):
    assert Solution().combine(n, k) == expected
