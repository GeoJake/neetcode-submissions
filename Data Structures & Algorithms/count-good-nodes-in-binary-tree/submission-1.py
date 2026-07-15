# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, curr_max: int):
            if not root:
                return 0

            out = 1 if root.val >= curr_max else 0
            curr_max = max(root.val, curr_max)
            
            out += dfs(root.left, curr_max)
            out += dfs(root.right, curr_max)

            return out
        
        return dfs(root, float("-inf"))