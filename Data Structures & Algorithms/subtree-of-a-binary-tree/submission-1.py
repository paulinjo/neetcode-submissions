# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False


        same = True
        def check_equal(n1: Optional[TreeNode], n2: Optional[TreeNode]):
            nonlocal same
            if not same:
                return

            if not n1 and not n2:
                return
            
            if (n1 and not n2) or (n2 and not n1):
                same = False
                return

            assert n1 and n2

            if n1.val != n2.val:
                same = False
                return
            
            check_equal(n1.left, n2.left)
            check_equal(n1.right, n2.right)

        possible_roots = []
        def locate_subtree_root(n: Optional[TreeNode], subRoot: TreeNode):
            nonlocal possible_roots

            if not n:
                return n

            if n.val == subRoot.val:
                possible_roots.append(n)
            
            locate_subtree_root(n.left, subRoot) 
            locate_subtree_root(n.right, subRoot)

        locate_subtree_root(root, subRoot)
        while possible_roots:
            same = True
            subRoot2 = possible_roots.pop()
            check_equal(subRoot, subRoot2)
            if same:
                return True
        return False
