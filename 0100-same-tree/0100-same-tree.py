from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(level_list: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order list where None represents a missing node."""
    if not level_list:
        return None
    it = iter(level_list)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    queue = deque([root])
    for val in it:
        parent = queue[0]  # peek current parent
        # fill left child
        if parent.left is None:
            if val is not None:
                parent.left = TreeNode(val)
                queue.append(parent.left)
            else:
                parent.left = None
            continue
        # fill right child
        if parent.right is None:
            if val is not None:
                parent.right = TreeNode(val)
                queue.append(parent.right)
            else:
                parent.right = None
            # finished both children for this parent, pop it
            queue.popleft()
    return root

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive DFS check: both None -> True; one None -> False; values differ -> False.
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# --- Example tests ---
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1,2,3], [1,2,3]),           # True
        ([1,2], [1,None,2]),          # False
        ([1,2,1], [1,1,2])            # False
    ]

    for idx, (a, b) in enumerate(tests, 1):
        p = build_tree(a)
        q = build_tree(b)
        print(f"Example {idx}: isSameTree({a}, {b}) -> {sol.isSameTree(p, q)}")
