import pytest
from maximum_depth_of_binary_tree import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, expected', [
    ([3,9,20,None,None,15,7], 3),
    ([1,None,2], 2),
    ([1], 1),
    ([], 0),
])
def test_solution(arr, expected):
    root = TreeNode.from_array(arr=arr)
    assert Solution().maxDepth(root) == expected
