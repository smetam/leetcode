import pytest
from remove_duplicates_from_sorted_list import Solution
from helpers.listnode import array_to_linked_list


@pytest.mark.parametrize('arr, expected', [
    ([1,1,2], [1,2]),
    ([1,1,2,3,3], [1,2,3]),
])
def test_solution(arr, expected):
    head = array_to_linked_list(arr)
    expected = array_to_linked_list(expected)
    assert Solution().deleteDuplicates(head) == expected
