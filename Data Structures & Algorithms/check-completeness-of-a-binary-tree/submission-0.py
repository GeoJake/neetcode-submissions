# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        oneChildNode = False

        while q:
            node = q.popleft()
            if oneChildNode:
                if node.left or node.right:
                    return False
            else:
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
                elif node.left and not node.right:
                    q.append(node.left)
                    oneChildNode = True
                elif not node.left and node.right:
                    return False
                else:
                    oneChildNode = True

        return True