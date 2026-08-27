from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional['ListNode'] = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's cycle-finding algorithm
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # move slow by 1
            fast = fast.next.next     # move fast by 2
            if slow == fast:
                return True
        return False
