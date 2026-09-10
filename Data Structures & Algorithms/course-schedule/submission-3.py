class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        courseDep = {}

        for p in prerequisites:
            if p[0] not in courseDep:
                courseDep[p[0]] = []
            courseDep[p[0]].append(p[1])

        def dfs(i):
            if i in visiting:
                return False

            if i not in courseDep or not len(courseDep[i]):
                return True

            visiting.add(i)
            
            for j in courseDep[i]:
                if not dfs(j):
                    return False
            
            visiting.remove(i)
            courseDep[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
        