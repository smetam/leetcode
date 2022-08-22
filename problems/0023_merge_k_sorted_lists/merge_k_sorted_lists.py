from typing import List, Optional
from heapq import heapify, heappop, heappush
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f'ListNode(val={self.val}, next={self.next})'

class NodeWrapper:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __lt__(self, other) -> bool:
        return self.val < other.val

    def __repr__(self) -> str:
        return f'NodeWrapper(val={self.val}, next={self.next})'


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root_node = ListNode()
        h = [NodeWrapper(l.val, l.next) for l in lists if l is not None]
        heapify(h)
        current_node = root_node
        while h:
            node = heappop(h)
            if node.next is not None:
                next_node = node.next
                heappush(h, NodeWrapper(next_node.val, next_node.next))
            current_node.next = node
            current_node = node
        return root_node.next






lists = [
    ListNode(val=1, next=
        ListNode(val=4, next=
            ListNode(val=5, next=None))), 
    ListNode(val=1, next=
        ListNode(val=3, next=
            ListNode(val=4, next=None))), 
    ListNode(val=2, next=
        ListNode(val=6, next=None))
]

Solution().mergeKLists(lists)
