import pytest
from insert_into_a_binary_search_tree import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, val, expected', [
    ([4,2,7,1,3], 5, [4,2,7,1,3,5]),
    ([40,20,60,10,30,50,70], 25, [40,20,60,10,30,50,70,None,None,25]),
    ([4,2,7,1,3,None,None,None,None,None,None], 5, [4,2,7,1,3,5])
])
def test_solution(arr, val, expected):
    root = TreeNode.from_array(arr)
    expected = TreeNode.from_array(expected)
    assert Solution().insertIntoBST(root, val) == expected
