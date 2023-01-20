import pytest
from best_sightseeing_pair import Solution


@pytest.mark.parametrize('values, expected', [
    ([8,1,5,2,6], 11),
    ([1, 2], 2),
    ([4,7,5,8], 13),
])
def test_solution(values, expected):
    assert Solution().maxScoreSightseeingPair(values) == expected
