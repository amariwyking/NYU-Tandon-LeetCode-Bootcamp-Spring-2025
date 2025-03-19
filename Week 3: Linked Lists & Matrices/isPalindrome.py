from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    slow_ptr = fast_ptr = head

    # Find the middle of the linked list using a pair of fast and slow pointers
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # Set current to the middle of the linked list
    curr = slow_ptr

    # We will reverse the second half of the linked list
    prev = None

    while curr:
        # store next node before disconnecting current node
        next_ptr = curr.next
        curr.next = prev

        # update the previous and curr nodes
        prev = curr
        curr = next_ptr

    # now check if the two halves are equivalent
    while prev:
        if prev.val != head.val:
            return False

        prev = prev.next
        head = head.next

    return True