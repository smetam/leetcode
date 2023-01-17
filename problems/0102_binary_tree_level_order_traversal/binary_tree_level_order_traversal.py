from typing import List, Optional
from helpers.treenode import TreeNode
from collections import deque, defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([(root, 0)])
        node_levels = defaultdict(list)
        max_depth = 0
        while len(q) > 0:
            node, level = q.popleft()
            max_depth = max(max_depth, level)
            node_levels[level].append(node.val)
            for child in (node.left, node.right):
                if child is not None:
                    q.append((child, level + 1))
        res = []
        for level in range(max_depth + 1):
            res.append(node_levels[level])
        return res
        
