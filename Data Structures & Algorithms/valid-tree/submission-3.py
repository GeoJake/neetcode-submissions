class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {}
        vertices = set()
        seen = set()

        if not edges:
            return True

        for e in edges:
            if e[0] not in adj_list:
                adj_list[e[0]] = []
            if e[1] not in adj_list:
                adj_list[e[1]] = []
            
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
            
            vertices.add(e[0])
            vertices.add(e[1])

        def dfs(i, prev, visited):
            if i in visited:
                return False
            
            visited.add(i)
            seen.add(i)
            
            for j in adj_list[i]:
                if not j == prev and not dfs(j, i, visited):
                    return False
            
            visited.remove(i)
            return True
        
        return dfs(0, 0, set()) and len(seen) == len(vertices)