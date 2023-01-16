import pytest
from convert_binary_number_in_a_linked_list_to_integer import Solution
from helpers.listnode import array_to_linked_list


@pytest.mark.parametrize('arr, expected', [
    ([1,0,1], 5),
    ([0], 0),
])
def test_solution(arr, expected):
    head = array_to_linked_list(arr)
    assert Solution().getDecimalValue(head) == expected
