import pytest
from middle_of_the_linked_list import Solution, ListNode


def array_to_linked_list(arr: list) -> ListNode:
    if len(arr) == 0:
        return None
    head = ListNode(val=arr[0])
    prev = head
    for val in arr[1:]:
        node = ListNode(val=val)
        prev.next = node
        prev = node
    return head


@pytest.mark.parametrize('arr, expected', [
    ([1,2,3,4,5], [3,4,5]),
    ([1,2,3,4,5,6], [4,5,6]),
])
def test_solution(arr, expected):
    node = array_to_linked_list(arr)
    expected = array_to_linked_list(expected)
    print(node)
    print(expected)
    print(Solution().middleNode(node))
    assert Solution().middleNode(node) == expected
