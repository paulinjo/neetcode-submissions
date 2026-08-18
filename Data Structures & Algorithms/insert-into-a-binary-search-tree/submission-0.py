# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def do_insert(node: TreeNode):
            nonlocal val

            if node.val < val:
                if node.right:
                    do_insert(node.right)
                else:
                    node.right = TreeNode(val)
            else:
                if node.left:
                    do_insert(node.left)
                else:
                    node.left = TreeNode(val)

        
        if not root:
            return TreeNode(val)

        do_insert(root)
        return root