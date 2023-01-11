from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def list_to_tree(arr) -> Node:
    if len(arr) == 0:
        return None
    root = Node(val=arr[0])
    if len(arr) == 1:
        return root
    q = deque()
    node = root
    children = []
    for elem in (arr[2:] + [None]):
        if elem is None:
            node.children = [Node(val=child) for child in children]
            q.extend(node.children)
            children = []
            node = q.popleft()
        else:
            children.append(elem)
    return root


class Solution:
    def preorder(self, root) -> List[int]:
        if root is None:
            return []
        order = []
        q = [root]
        while len(q) > 0:
            node = q.pop()
            order.append(node.val)
            if node.children:
                for child in reversed(node.children):
                    q.append(child)
        return order
