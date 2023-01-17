import pytest
from binary_tree_level_order_traversal import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, expected', [
    ([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]),
    ([1], [[1]]),
    ([], []),
])
def test_solution(arr, expected):
    root = TreeNode.from_array(arr)
    assert Solution().levelOrder(root) == expected
