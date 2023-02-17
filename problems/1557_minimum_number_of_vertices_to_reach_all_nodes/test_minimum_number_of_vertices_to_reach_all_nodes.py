import pytest
from minimum_number_of_vertices_to_reach_all_nodes import Solution


@pytest.mark.parametrize('n, edges, expected', [
    (6, [[0,1],[0,2],[2,5],[3,4],[4,2]], [0,3]),
    (5, [[0,1],[2,1],[3,1],[1,4],[2,4]], [0,2,3]),
])
def test_solution(n, edges, expected):
    assert set(Solution().findSmallestSetOfVertices(n, edges)) == set(expected)
