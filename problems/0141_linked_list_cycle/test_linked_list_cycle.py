import pytest
from linked_list_cycle import Solution
from helpers.listnode import array_to_linked_list, get_last_node, get_node_by_idx


@pytest.mark.parametrize('arr, pos, expected', [
    ([3,2,0,-4], 1, True),
    ([1,2], 0, True),
    ([1], -1, False),
])
def test_solution(arr, pos, expected):
    node = array_to_linked_list(arr)
    last_node = get_last_node(node)
    if pos >= 0:
        repeating_node = get_node_by_idx(node, pos)
        last_node.next = repeating_node
    assert Solution().hasCycle(node) == expected
