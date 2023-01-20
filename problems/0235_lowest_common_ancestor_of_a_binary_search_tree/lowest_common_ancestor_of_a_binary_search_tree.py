from helpers.treenode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val = root.val

        if (q.val - val) * (p.val - val) <= 0:
            # means one of q, p is equal to val
            # or they are in different subtrees
            return root

        # here they are in same subtree
        if q.val > val:
            # means they are both right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        
        # means they are both left subtree
        return self.lowestCommonAncestor(root.left, p, q)
