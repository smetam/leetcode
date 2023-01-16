import pytest
from merge_two_binary_trees import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr1, arr2, expected', [
    ([1,3,2,5], [2,1,3,None,4,None,7], [3,4,5,5,4,None,7]),
    ([1], [1,2], [2,2]),
    ([1,3,2,5], [], [1,3,2,5]),
    ([], [1,3,2,5], [1,3,2,5]),
    ([], [], []),
])
def test_solution(arr1, arr2, expected):
    root1 = TreeNode.from_array(arr1)
    root2 = TreeNode.from_array(arr2)
    expected = TreeNode.from_array(expected)
    assert Solution().mergeTrees(root1, root2) == expected
