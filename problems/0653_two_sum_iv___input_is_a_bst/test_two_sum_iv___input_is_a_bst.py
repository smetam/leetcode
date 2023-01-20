import pytest
from two_sum_iv___input_is_a_bst import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, k, expected', [
    ([5,3,6,2,4,None,7], 9, True),
    ([5,3,6,2,4,None,7], 28, False),
])
def test_solution(arr, k, expected):
    root = TreeNode.from_array(arr)
    assert Solution().findTarget(root, k) == expected
