import pytest
from validate_binary_search_tree import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, expected', [
    ([2,1,3], True),
    ([5,1,4,None,None,3,6], False),
])
def test_solution(arr, expected):
    root = TreeNode.from_array(arr)
    assert Solution().isValidBST(root) == expected
