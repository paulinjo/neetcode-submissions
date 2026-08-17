# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return node
            
            tmp = node.left
            node.left = node.right
            node.right = tmp

            invert(node.left)
            invert(node.right)
            return node

        invert(root)
        return root