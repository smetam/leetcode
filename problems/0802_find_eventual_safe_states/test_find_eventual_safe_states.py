import pytest
from find_eventual_safe_states import Solution


@pytest.mark.parametrize('graph, expected', [
    ([[1,2],[2,3],[5],[0],[5],[],[]], [2,4,5,6]),
    ([[1,2,3,4],[1,2],[3,4],[0,4],[]], [4]),
])
def test_solution(graph, expected):
    assert Solution().eventualSafeNodes(graph) == expected
