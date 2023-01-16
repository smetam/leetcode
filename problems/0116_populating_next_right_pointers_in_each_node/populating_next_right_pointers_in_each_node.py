from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __eq__(self, other: 'Node') -> bool:
        if self.val != other.val:
            print(f'Values dont match: {self.val}, {other.val}')
            return False
        if self.left != other.left:
            print(f'Left dont match: {self.left}, {other.left}')
            return False
        if self.right != other.right:
            print(f'Right dont match: {self.right}, {other.right}')
            return False
        if self.next != other.next:
            print(f'Next dont match: {self.next}, {other.next}')
            return False
        return True 

    def __str__(self) -> str:
        return f'Node({self.val}, left={self.left}, right={self.right}, next={self.next})'

    def __repr__(self) -> str:
        return str(self)


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None: 
            return None
        left = root.left
        right = root.right
        self.connect(left)
        self.connect(right)
        while left is not None and right is not None:
            left.next = right
            left = left.right
            right = right.left
        return root
