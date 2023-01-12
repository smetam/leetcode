from typing import Optional
from helpers.listnode import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        n_nodes = 0
        while node is not None:
            node = node.next
            n_nodes += 1
        node_remove_idx = n_nodes - n 
        if node_remove_idx == 0:
            return head.next
        node = head
        for _ in range(node_remove_idx - 1):
            node = node.next
        node.next = node.next.next
        return head