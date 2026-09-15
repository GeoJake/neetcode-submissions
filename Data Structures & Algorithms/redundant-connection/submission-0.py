class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj_list = [[] for _ in range(len(edges) + 1)]

        def dfs(curr, prev):

            if curr in seen:
                return True
            
            seen.add(curr)

            for i in adj_list[curr]:
                if i == prev:
                    continue
                if dfs(i, curr):
                    return True
            return False
            

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            seen = set()

            if dfs(u, -1):
                return [u, v]
        
        return []