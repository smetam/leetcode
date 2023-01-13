from typing import Optional
from helpers.listnode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast_node = head
        slow_node = head
        step = 0
        while fast_node.next is not None:
            fast_node = fast_node.next
            if step % 2 == 1:
                slow_node = slow_node.next
            step += 1
            if fast_node is slow_node:
                return True
        return False