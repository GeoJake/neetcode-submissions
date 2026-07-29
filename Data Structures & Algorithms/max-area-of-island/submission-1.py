class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or not grid[r][c]:
                return 0
            
            grid[r][c] = 0

            return 1 + dfs(r-1,c) + dfs(r,c-1) + dfs(r,c+1) + dfs(r+1,c)

        
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r,c))

        return maxArea