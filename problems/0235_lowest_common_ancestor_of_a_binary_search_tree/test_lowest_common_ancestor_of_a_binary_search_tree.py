import pytest
from lowest_common_ancestor_of_a_binary_search_tree import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, p, q, expected', [
    ([6,2,8,0,4,7,9,None,None,3,5], 2, 8, 6),
    ([6,2,8,0,4,7,9,None,None,3,5], 2, 4, 2),
    ([2,1], 2, 1, 2),
])
def test_solution(arr, p, q, expected):
    root = TreeNode.from_array(arr)
    p = TreeNode(val=p)
    q = TreeNode(val=q)
    assert Solution().lowestCommonAncestor(root, p, q).val == expected
