import pytest
from number_of_operations_to_make_network_connected import Solution


@pytest.mark.parametrize('n, connections, expected', [
    (4, [[0,1],[0,2],[1,2]], 1),
    (6, [[0,1],[0,2],[0,3],[1,2],[1,3]], 2),
    (6, [[0,1],[0,2],[0,3],[1,2]], -1),
    (11, [[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]], 3)
])
def test_solution(n, connections, expected):
    assert Solution().makeConnected(n, connections) == expected
