# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow_ptr, fast_ptr = head, head.next

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # Set current node to the center
    second = slow_ptr.next
    prev = slow_ptr.next = None

    # Reverse the second half of the list
    while second:
        tmp = second.next
        second.next = prev

        prev = second
        second = tmp

    left_ptr = head
    right_ptr = prev

    # Reorder by alternating selections from each half
    while right_ptr:
        tmp1, tmp2 = left_ptr.next, right_ptr.next

        left_ptr.next = right_ptr
        right_ptr.next = tmp1

        left_ptr = tmp1
        right_ptr = tmp2