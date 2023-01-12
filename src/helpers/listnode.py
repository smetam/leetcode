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


def array_to_linked_list(arr: list) -> ListNode:
    if len(arr) == 0:
        return None
    head = ListNode(val=arr[0])
    prev = head
    for val in arr[1:]:
        node = ListNode(val=val)
        prev.next = node
        prev = node
    return head
