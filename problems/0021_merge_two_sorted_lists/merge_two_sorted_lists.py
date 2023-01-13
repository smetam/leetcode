from typing import Optional
from helpers.listnode import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        current_node = head
        while (list1 is not None) and (list2 is not None):
            if list1.val < list2.val:
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next
            current_node.next = next_node
            current_node = next_node

        if list1 is None:
            current_node.next = list2
        if list2 is None:
            current_node.next = list1
        return head