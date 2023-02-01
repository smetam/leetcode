import pytest
from nearest_exit_from_entrance_in_maze import Solution


@pytest.mark.parametrize('maze, entrance, expected', [
    ([
        ["+","+",".","+"],
        [".",".",".","+"],
        ["+","+","+","."],
    ], [1,2], 1),
    ([
        ["+","+","+"],
        [".",".","."],
        ["+","+","+"],
    ], [1,0], 2),
])
def test_solution(maze, entrance, expected):
    assert Solution().nearestExit(maze, entrance) == expected
