# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
        out = []

        def right_dfs(root, depth):
            if not root:
                return None

            if depth == len(out):
                out.append(root.val)
            
            right_dfs(root.right, depth + 1)
            right_dfs(root.left, depth + 1)

        right_dfs(root, 0)

        return out