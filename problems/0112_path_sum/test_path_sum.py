import pytest
from path_sum import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, targetSum, expected', [
    ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22, True),
    ([1,2,3], 5, False),
    ([], 0, False)
])
def test_solution(arr, targetSum, expected):
    root = TreeNode.from_array(arr)
    assert Solution().hasPathSum(root, targetSum) == expected
