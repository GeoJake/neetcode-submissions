class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        takenCourses = set()
        courseDep = {}
        res = True

        def dfs(i, seen):
            nonlocal res

            if not res or i in takenCourses:
                return

            if i in seen:
                res = False
                return

            if i not in courseDep or not len(courseDep[i]):
                takenCourses.add(i)
                return

            seen.add(i)
            
            for j in courseDep[i]:
                dfs(j, seen)
            
            seen.remove(i)
            courseDep[i] = set()

        for p in prerequisites:
            if p[0] not in courseDep:
                courseDep[p[0]] = set()
            courseDep[p[0]].add(p[1])

        for i in range(numCourses):
            if not res:
                return res
            dfs(i, set())
            
        return res
        