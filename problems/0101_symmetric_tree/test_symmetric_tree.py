import pytest
from symmetric_tree import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, expected', [
    ([1,2,2,3,4,4,3], True),
    ([1,2,2,None,3,None,3], False),
])
def test_solution(arr, expected):
    root = TreeNode.from_array(arr)
    assert Solution().isSymmetric(root) == expected
