import pytest
from merge_two_sorted_lists import Solution
from helpers.listnode import array_to_linked_list


@pytest.mark.parametrize('list1, list2, expected', [
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], []),
    ([], [0], [0]),
])
def test_solution(list1, list2, expected):
    list1 = array_to_linked_list(list1)
    list2 = array_to_linked_list(list2)
    expected = array_to_linked_list(expected)
    assert Solution().mergeTwoLists(list1, list2) == expected
