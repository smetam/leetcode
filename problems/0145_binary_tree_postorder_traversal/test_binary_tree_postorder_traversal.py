import pytest
from binary_tree_postorder_traversal import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, expected', [
    ([1,None, 2, None, None, 3], [3,2,1]),
    ([], []),
    ([1], [1]),
])
def test_solution(arr, expected):
    root = TreeNode.from_array(arr)
    assert Solution().postorderTraversal(root) == expected