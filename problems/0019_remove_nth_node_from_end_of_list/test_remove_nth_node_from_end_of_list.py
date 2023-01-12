import pytest
from remove_nth_node_from_end_of_list import Solution
from helpers.listnode import array_to_linked_list


@pytest.mark.parametrize('arr, n, expected', [
    ([1,2,3,4,5], 2, [1,2,3,5]),
    ([1], 1, []),
    ([1,2], 1, [1]),
])
def test_solution(arr, n, expected):
    node = array_to_linked_list(arr)
    expected = array_to_linked_list(expected)
    assert Solution().removeNthFromEnd(node, n) == expected
