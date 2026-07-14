# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        curr = deque([root])

        while curr:
            level = []
            curr_len = len(curr)
            for i in range(curr_len):
                curr_node = curr.pop()
                if curr_node:
                    level.append(curr_node.val)
                    curr.appendleft(curr_node.left)
                    curr.appendleft(curr_node.right)
            if level:
                res.append(level)
    
        return res
            