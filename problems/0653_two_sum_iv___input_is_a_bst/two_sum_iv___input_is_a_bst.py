from typing import Optional
from helpers.treenode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def forward_traversal(root):
            if root is not None:
                yield from forward_traversal(root.left)
                yield root.val
                yield from forward_traversal(root.right)

        def backward_traversal(root):
            if root is not None:
                yield from backward_traversal(root.right)
                yield root.val
                yield from backward_traversal(root.left)
        
        # move pointers from both side until they meet
        left_gen = forward_traversal(root)
        right_gen = backward_traversal(root)

        left, right = next(left_gen), next(right_gen)
        while left < right:
            current_sum = left + right
            if current_sum == k: 
                return True
            if current_sum < k:
                left = next(left_gen)
            else:
                right = next(right_gen)
        return False

