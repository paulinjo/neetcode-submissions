# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same = True
        
        def compare(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> None:
            nonlocal is_same
            
            if not n1 and not n2:
                return
            
            if n1 and not n2 or n2 and not n1:
                is_same = False
                return

            assert n1 and n2
            if n1.val != n2.val:
                is_same = False
                return

            compare(n1.left, n2.left)
            compare(n1.right, n2.right)
        
        compare(p, q)
        return is_same