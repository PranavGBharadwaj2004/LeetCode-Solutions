# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting point of the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Iterate as long as there are nodes in l1 or l2, or a carry exists
        while l1 or l2 or carry:
            # Get values from nodes, or 0 if we've reached the end of a list
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Add the digit to our result list
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to next nodes if possible
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
