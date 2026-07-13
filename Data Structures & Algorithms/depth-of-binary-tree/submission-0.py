# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0

        def dfs(node, height):
            if not node:
                return height
            
            height += 1
            
            return max(dfs(node.left, height), dfs(node.right, height))
        
        
        
        return dfs(root, height)