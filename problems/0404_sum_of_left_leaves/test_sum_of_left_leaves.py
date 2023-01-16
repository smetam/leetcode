import pytest
from sum_of_left_leaves import Solution
from helpers.treenode import TreeNode


@pytest.mark.parametrize('arr, expected', [
    ([3,9,20,None,None,15,7], 24),
    ([1], 0),
    ([], 0),
    ([1,2], 2),
])
def test_solution(arr, expected):
    root = TreeNode.from_array(arr)
    assert Solution().sumOfLeftLeaves(root) == expected
