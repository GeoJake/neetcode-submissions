class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        tree = {}

        for a, b in edges:
            if a not in tree:
                tree[a] = set()
            if b not in tree:
                tree[b] = set()
            tree[a].add(b)
            tree[b].add(a)
        
        def dfs(i, par):
            time = 0

            if i not in tree:
                return time
    
            for j in tree[i]:
                if j == par:
                    continue
                childTime = dfs(j, i)
                if childTime > 0 or hasApple[j]:
                    time += 2 + childTime
            
            return time
        
        return dfs(0, -1)