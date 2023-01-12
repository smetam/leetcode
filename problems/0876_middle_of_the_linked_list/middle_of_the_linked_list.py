from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f'ListNode({self.val}, next={self.next})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return (self.val == other.val) and (self.next == other.next)
        


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        step = 0
        while node is not None:
            node = node.next
            step += 1
        step = step // 2
        for _ in range(step):
            head = head.next
        return head
        
