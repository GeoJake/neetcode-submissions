# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([(0, root)])
        curr_depth = 0
        level_max = root.val
        res = []

        while q:
            depth, curr = q.popleft()

            if depth > curr_depth:
                res.append(level_max)
                curr_depth = depth
                level_max = curr.val

            level_max = max(level_max, curr.val)

            if curr.left:
                q.append((curr_depth + 1, curr.left))

            if curr.right:
                q.append((curr_depth + 1, curr.right))
        
        res.append(level_max)

        return res