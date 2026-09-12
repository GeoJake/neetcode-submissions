class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        seen = set()
        adj_list = {}

        for e in edges:
            if not e[0] in adj_list:
                adj_list[e[0]] = []
            if not e[1] in adj_list:
                adj_list[e[1]] = []
            
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])

        def dfs(i, prev, seen):
            if i in seen:
                return
            
            seen.add(i)

            if i not in adj_list:
                return

            for j in adj_list[i]:
                if not j == prev:
                    dfs(j, i, seen)
            
            return
        
        for i in range(n):
            if not i in seen:
                dfs(i, i, seen)
                res += 1
        return res