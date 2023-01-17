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
    def tree_mirrored(cls, left: Optional[TreeNode], right: Optional[TreeNode]):
        if left is None and right is None:
            return True
        if left is not None and right is not None:
            return (left.val == right.val) \
                and cls.tree_mirrored(left.left, right.right) \
                and cls.tree_mirrored(left.right, right.left)
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.tree_mirrored(root.left, root.right)
        

        
        