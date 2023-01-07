import pytest
from first_bad_version import Solution

@pytest.mark.parametrize('n, expected', [
    (5, 4),
    (1, 1),
])
def test_solution(n, expected):
    def isBadVersion(version: int) -> bool:
        return version == expected
        
    assert Solution().firstBadVersion(n, isBadVersion) == expected
