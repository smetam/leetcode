import pytest
from unique_binary_search_trees import Solution


@pytest.mark.parametrize('n, expected', [
    (1, 1),
    (2, 2),
    (3, 5),
])
def test_solution(n, expected):
    assert Solution().numTrees(n) == expected
