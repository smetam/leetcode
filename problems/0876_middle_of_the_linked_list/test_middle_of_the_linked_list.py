import pytest
from middle_of_the_linked_list import Solution
from helpers.listnode import array_to_linked_list


@pytest.mark.parametrize('arr, expected', [
    ([1,2,3,4,5], [3,4,5]),
    ([1,2,3,4,5,6], [4,5,6]),
])
def test_solution(arr, expected):
    node = array_to_linked_list(arr)
    expected = array_to_linked_list(expected)
    assert Solution().middleNode(node) == expected
