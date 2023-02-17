import pytest
from minimum_genetic_mutation import Solution


@pytest.mark.parametrize('startGene, endGene, bank, expected', [
    ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
    ("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2),
])
def test_solution(startGene, endGene, bank, expected):
    assert Solution().minMutation(startGene, endGene, bank) == expected
