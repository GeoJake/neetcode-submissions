class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        p = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or not grid[r][c]:
                return 1

            if (r, c) in visit:
                return 0
            
            visit.add((r, c))
            
            return dfs(r, c-1) + dfs(r, c+1) + dfs(r-1, c) + dfs(r+1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r,c)

        return 0

            