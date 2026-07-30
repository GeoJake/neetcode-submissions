# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(root, total):
            total += root.val

            if not root.left and not root.right:
                return total == targetSum
            
            b_l = b_r = False

            if root.left:
                b_l = helper(root.left, total)
            if root.right:
                b_r = helper(root.right, total)

            return b_l or b_r
        
        return helper(root, 0) if root else False