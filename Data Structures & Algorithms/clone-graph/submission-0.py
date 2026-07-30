"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}
        
        def dfs(node):
            if not node:
                return
            if not node in graph:
                graph[node.val] = Node(node.val)
            for n in node.neighbors:
                if not n.val in graph:
                    graph[n.val] = Node(n.val)
                    dfs(n)
                graph[node.val].neighbors.append(graph[n.val])
        
        dfs(node)

        return graph[1] if 1 in graph else None