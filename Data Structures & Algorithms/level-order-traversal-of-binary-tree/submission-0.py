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
        child = deque([])

        while curr or child:
            new_list = []

            while curr:
                curr_node = curr.pop()

                if curr_node.left:
                    child.appendleft(curr_node.left)
                if curr_node.right:
                    child.appendleft(curr_node.right)

                new_list.append(curr_node.val)

            res.append(new_list)

            curr = child
            child = deque([])
    
        return res
            