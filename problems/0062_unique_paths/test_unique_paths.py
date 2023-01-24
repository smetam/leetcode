import pytest
from unique_paths import Solution


@pytest.mark.parametrize('m, n, expected', [
    (3, 7, 28),
    (3, 2, 3),
])
def test_solution(m, n, expected):
    assert Solution().uniquePaths(m, n) == expected
