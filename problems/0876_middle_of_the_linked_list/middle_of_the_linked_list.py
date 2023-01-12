from typing import Optional
from helpers.listnode import ListNode


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
        
