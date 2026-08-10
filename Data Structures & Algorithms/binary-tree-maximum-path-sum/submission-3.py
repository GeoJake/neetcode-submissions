# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxPath = root.val

        def calculateMaxPath(root):
            nonlocal maxPath
            if not root:
                return 0
            
            left = max(calculateMaxPath(root.left), 0)
            right = max(calculateMaxPath(root.right), 0)
            maxPath = max(maxPath, root.val + left + right)

            return root.val + max(left, right)
        
        calculateMaxPath(root)

        return maxPath