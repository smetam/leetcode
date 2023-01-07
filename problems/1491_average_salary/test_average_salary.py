import pytest
from average_salary import Solution


@pytest.mark.parametrize('salary, expected', [
    ([4000,3000,1000,2000], 2500),
    ([1000,2000,3000], 2000),
])
def test_solution(salary, expected):
    assert abs(Solution().average(salary) - expected) < 1e-5
