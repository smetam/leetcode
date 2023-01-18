import pytest
from invert_binary_tree import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, expected', [
    ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
    ([2,1,3], [2,3,1]),
    ([], [])
])
def test_solution(arr, expected):
    root = TreeNode.from_array(arr)
    expected = TreeNode.from_array(expected)
    assert Solution().invertTree(root) == expected
