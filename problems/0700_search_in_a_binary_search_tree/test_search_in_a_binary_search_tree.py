import pytest
from search_in_a_binary_search_tree import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, val, expected', [
    ([4,2,7,1,3], 2, [2,1,3]),
    ([4,2,7,1,3], 5, []),
])
def test_solution(arr, val, expected):
    root = TreeNode.from_array(arr)
    expected = TreeNode.from_array(expected)
    assert Solution().searchBST(root, val) == expected
