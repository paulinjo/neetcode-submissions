# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node: Optional[TreeNode], upper_bound: int, lower_bound: int) -> bool:
            if not node:
                return True
            
            # print(f"{node.val=} | {upper_bound=} | {lower_bound=}")

            if node.val >= upper_bound or node.val <= lower_bound:
                return False
            
            return check(node.left, min(upper_bound, node.val), lower_bound) and check(node.right, upper_bound, max(lower_bound, node.val))
        
        return check(root, float('inf'), float('-inf'))