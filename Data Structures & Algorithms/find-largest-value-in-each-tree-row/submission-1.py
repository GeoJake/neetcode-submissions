# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        nodes = [root] if root else []
        
        while nodes:
            res.append(max(node.val for node in nodes))
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
        return res