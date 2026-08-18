# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []

        def traverse(node: Optional[TreeNode], level: int):
            if not node:
                return

            nonlocal results
            if len(results) - 1 < level:
                results.append([])
            
            results[level].append(node.val)
            
            traverse(node.left, level+1)
            traverse(node.right, level+1)
        
        traverse(root, 0)
        return results