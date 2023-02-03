import pytest
from time_needed_to_inform_all_employees import Solution


@pytest.mark.parametrize('n, headID, manager, informTime, expected', [
    (1, 0, [-1], [0], 0),
    (6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0], 1),
])
def test_solution(n, headID, manager, informTime, expected):
    assert Solution().numOfMinutes(n, headID, manager, informTime) == expected
