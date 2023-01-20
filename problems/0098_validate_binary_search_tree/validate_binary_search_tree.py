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
    def _is_valid(cls, root: Optional[TreeNode], min_limit: int = None, max_limit: int = None) -> bool:
        if root is None:
            return True
        val = root.val

        if min_limit is not None and val < min_limit:
                return False

        if max_limit is not None and val > max_limit:
            return False 

        if not cls._is_valid(root.left, min_limit=min_limit, max_limit=val - 1):
            return False
        if not cls._is_valid(root.right, min_limit=val + 1, max_limit=max_limit):
            return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._is_valid(root)
