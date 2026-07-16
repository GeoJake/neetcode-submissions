"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        out = []

        def dfs(root: 'Node'):
            nonlocal out
            if root:
                for c in root.children:
                    dfs(c)
                out.append(root.val)
        dfs(root)

        return out