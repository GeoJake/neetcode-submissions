class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        calcPath = [[-1] * COLS for i in range(ROWS)]

        def dfs(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]

            if r == ROWS or c == COLS:
                return float("inf")
            
            if calcPath[r][c] != -1:
                return calcPath[r][c]

            calcPath[r][c] = grid[r][c] + min(dfs(r+1, c), dfs(r, c+1))
            return calcPath[r][c]

        return dfs(0, 0)