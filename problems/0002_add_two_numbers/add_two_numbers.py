from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def step(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        val = l1.val + l2.val + carry
        val, carry = val % 10, val // 10
        
        if l1.next is None and l2.next is None and (carry == 0):
            return ListNode(val=val, next=None)
        
        l1 = l1.next or ListNode()
        l2 = l2.next or ListNode()
        next_node = self.step(l1, l2, carry=carry)
        
        return ListNode(val=val, next=next_node)
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.step(l1, l2)