# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """

        in: root of tree
        out: total number of good nodes
        edge: root is the only node

        """

        out = 0

        def dfs(root: TreeNode, curr_max: int):
            nonlocal out
            if not root:
                return None
            
            if root.val >= curr_max:
                out += 1
                curr_max = root.val
            
            dfs(root.left, curr_max)
            dfs(root.right, curr_max)
        
        dfs(root, float("-inf"))
        return out