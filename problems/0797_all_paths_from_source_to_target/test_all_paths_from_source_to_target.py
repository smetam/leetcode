import pytest
from all_paths_from_source_to_target import Solution


@pytest.mark.parametrize('graph, expected', [
    ([[1,2],[3],[3],[]], [[0,1,3],[0,2,3]]),
    ([[4,3,1],[3,2,4],[3],[4],[]], [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]),
])
def test_solution(graph, expected):
    assert sorted(Solution().allPathsSourceTarget(graph)) == sorted(expected)
