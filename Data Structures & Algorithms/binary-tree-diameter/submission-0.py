# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal res
            
            if not node:
                return 0
            
            l, r = traverse(node.left), traverse(node.right)
            res = max(res, l+r)

            return 1 + max(l, r)
        
        traverse(root)
        return res