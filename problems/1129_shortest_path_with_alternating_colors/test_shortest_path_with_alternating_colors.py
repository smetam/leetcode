import pytest
from shortest_path_with_alternating_colors import Solution


@pytest.mark.parametrize('n, redEdges, blueEdges, expected', [
    (3, [[0,1],[1,2]], [], [0,1,-1]),
    (3, [[0,1]], [[2,1]], [0,1,-1]),
    (5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]], [0,1,2,3,7])
])
def test_solution(n, redEdges, blueEdges, expected):
    assert Solution().shortestAlternatingPaths(n, redEdges, blueEdges) == expected
