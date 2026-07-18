# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = root.val

        def dfs(root, k):
            nonlocal res
            if not root or not k:
                return k
            
            k = dfs(root.left, k)
            
            if not k:
                return 0

            k -= 1

            if not k:
                res = root.val
                return 0
        
            k = dfs(root.right, k)
            
            return k
        
        dfs(root, k)

        return res