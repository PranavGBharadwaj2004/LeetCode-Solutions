# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Two-pointer technique: slow moves one step, fast moves two steps.
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Helper to build a linked list from a Python list and return the head
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

# Helper to convert a linked list (starting at node) to a Python list
def list_to_array(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

if __name__ == "__main__":
    # Example 1
    head = build_list([1, 2, 3, 4, 5])
    mid = Solution().middleNode(head)
    print(list_to_array(mid))  # Output: [3, 4, 5]

    # Example 2
    head2 = build_list([1, 2, 3, 4, 5, 6])
    mid2 = Solution().middleNode(head2)
    print(list_to_array(mid2))  # Output: [4, 5, 6]
