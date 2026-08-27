# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        # simple representation for debugging
        vals = []
        node = self
        while node:
            vals.append(str(node.val))
            node = node.next
        return "[" + ", ".join(vals) + "]"

def build_list(values):
    """Builds a linked list from a Python list and returns the head (or None)."""
    if not values:
        return None
    head = ListNode(values[0])
    tail = head
    for v in values[1:]:
        tail.next = ListNode(v)
        tail = tail.next
    return head

def to_list(head):
    """Converts linked list to Python list (for easy checking)."""
    out = []
    node = head
    while node:
        out.append(node.val)
        node = node.next
    return out

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Iterative merge using a dummy node; reuses nodes from the input lists.
        dummy = ListNode(0)
        tail = dummy
        p, q = list1, list2

        while p and q:
            if p.val <= q.val:
                tail.next = p
                p = p.next
            else:
                tail.next = q
                q = q.next
            tail = tail.next

        # attach the remaining part
        tail.next = p if p else q
        return dummy.next

if __name__ == "__main__":
    s = Solution()

    # Example 1
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    merged = s.mergeTwoLists(l1, l2)
    print("Example 1 merged:", to_list(merged))  # [1,1,2,3,4,4]

    # Example 2
    l1 = build_list([])
    l2 = build_list([])
    merged = s.mergeTwoLists(l1, l2)
    print("Example 2 merged:", to_list(merged))  # []

    # Example 3
    l1 = build_list([])
    l2 = build_list([0])
    merged = s.mergeTwoLists(l1, l2)
    print("Example 3 merged:", to_list(merged))  # [0]
