import pytest
from linked_list_cycle_ii import Solution
from helpers.listnode import array_to_linked_list, get_last_node, get_node_by_idx


@pytest.mark.parametrize('arr, pos, expected', [
    ([3,2,0,-4], 1, 1),
    ([1,2], 0, 0),
    ([1], -1, None),
    ([], -1, None),
])
def test_solution(arr, pos, expected):
    node = array_to_linked_list(arr)
    if node is not None:
        last_node = get_last_node(node)
    if pos >= 0:
        repeating_node = get_node_by_idx(node, pos)
        last_node.next = repeating_node
        expected = repeating_node
    else:
        expected = None
    assert Solution().detectCycle(node) is expected
