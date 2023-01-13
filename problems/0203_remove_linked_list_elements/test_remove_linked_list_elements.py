import pytest
from remove_linked_list_elements import Solution
from helpers.listnode import array_to_linked_list


@pytest.mark.parametrize('arr, val, expected', [
    ([1,2,6,3,4,5,6], 6, [1,2,3,4,5]),
    ([], 1, []),
    ([7,7,7,7], 7, []),
])
def test_solution(arr, val, expected):
    head = array_to_linked_list(arr)
    expected = array_to_linked_list(expected)
    assert Solution().removeElements(head, val) == expected
