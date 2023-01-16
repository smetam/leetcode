from typing import Optional
from helpers.treenode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    @classmethod
    def sum_of_left_leaves(cls, root: TreeNode, is_left: bool) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val if is_left else 0
        return cls.sum_of_left_leaves(root.left, is_left=True) + cls.sum_of_left_leaves(root.right, is_left=False)


    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sum_of_left_leaves(root, is_left=False)
