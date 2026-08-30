# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
        
            if (a and not b) or (b and not a):
                return False
        
            if a.val != b.val:
                return False

            return traverse(a.left, b.left) and traverse(a.right, b.right)
        
        return traverse(p, q)