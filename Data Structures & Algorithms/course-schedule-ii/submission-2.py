class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]

        for e in prerequisites:
            adj_list[e[0]].append(e[1])

        seen, cycle = set(), set()

        def dfs(i) -> bool:
            if i in cycle:
                return False
            if i in seen:
                return True

            cycle.add(i)

            for j in adj_list[i]:
                if not dfs(j):
                    return False
            
            cycle.remove(i)
            seen.add(i)
            order.append(i)
            return True

            
        order = []

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order