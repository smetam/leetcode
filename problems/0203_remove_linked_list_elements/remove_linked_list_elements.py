from typing import List, Optional
from helpers.listnode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        prev = dummy
        curr = head
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else: 
                prev = curr
            curr = curr.next

        return dummy.next