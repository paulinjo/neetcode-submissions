import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        results = 0

        def traverse(node: Optional[TreeNode], max_val_seen: int):
            nonlocal results
            if not node:
                return

            if node.val >= max_val_seen:
                results += 1
            
            traverse(node.left, max(max_val_seen, node.val))
            traverse(node.right, max(max_val_seen, node.val))

        traverse(root, float('-inf'))
        return results