import pytest
from find_the_town_judge import Solution


@pytest.mark.parametrize('n, trust, expected', [
    (2, [[1,2]], 2),
    (3, [[1,3],[2,3]], 3),
    (3, [[1,3],[2,3],[3,1]], -1),
])
def test_solution(n, trust, expected):
    assert Solution().findJudge(n, trust) == expected
