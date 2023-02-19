from typing import Optional
from helpers.listnode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# requres O(1) space
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            # fast moves 2 times
            fast = fast.next.next
            # slow moves once
            slow = slow.next

            # when they meet
            if fast is slow:
                # slow has travelled (x + y), 
                # where x - number of nodes before cycle start 
                # and y is number of nodes after cycle start
                # fast has travelled 2 * (x + y)
                # this means that x + y = c * k
                # where c - is cycle lenght and k - is positive int
                # so if slow travels x - it will be in cycle start
                # and if we move head by x it will also be in cycle start
                while head is not slow:
                    head = head.next
                    slow = slow.next
                return head

        return None


# requres O(n) space
class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        fast = head
        slow = []
        step = 0
        while fast.next is not None:
            fast = fast.next
            for node in slow:
                if node is fast:
                    return node
            if step % 2 == 1:
                slow = [node.next for node in slow] + [head]
            step += 1
        return None
