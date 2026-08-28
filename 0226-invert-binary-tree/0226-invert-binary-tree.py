from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive solution: swap left and right for each node
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# Helper: build binary tree from level-order list (use None for missing nodes)
def build_tree_from_list(vals: List[Optional[int]]) -> Optional[TreeNode]:
    if not vals:
        return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    q = deque(nodes[1:])
    root = nodes[0]
    for node in nodes:
        if node:
            if q:
                node.left = q.popleft()
            if q:
                node.right = q.popleft()
    return root

# Helper: serialize tree to level-order list (trims trailing None)
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    out = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    # Trim trailing Nones
    while out and out[-1] is None:
        out.pop()
    return out

if __name__ == "__main__":
    sol = Solution()

    examples = [
        [4, 2, 7, 1, 3, 6, 9],
        [2, 1, 3],
        []
    ]

    for i, vals in enumerate(examples, 1):
        root = build_tree_from_list(vals)
        inverted = sol.invertTree(root)
        print(f"Example {i}: input = {vals} -> inverted = {tree_to_list(inverted)}")
