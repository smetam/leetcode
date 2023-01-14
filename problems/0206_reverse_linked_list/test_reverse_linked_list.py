import pytest
from reverse_linked_list import Solution
from helpers.listnode import array_to_linked_list


@pytest.mark.parametrize('arr, expected', [
    ([1,2,3,4,5], [5,4,3,2,1]),
    ([1,2], [2,1]),
    ([], []),
])
def test_solution(arr, expected):
    head = array_to_linked_list(arr)
    expected = array_to_linked_list(expected)
    assert Solution().reverseList(head) == expected
