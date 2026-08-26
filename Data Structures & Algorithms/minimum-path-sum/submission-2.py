class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        calcPath = [[-1] * COLS for i in range(ROWS)]

        def dfs(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]

            down = right = float("inf")

            if r + 1 < ROWS:
                if calcPath[r+1][c] > -1:
                    down = calcPath[r+1][c]
                else:
                    calcPath[r+1][c] = down = dfs(r + 1, c)
            if c + 1 < COLS:
                if calcPath[r][c+1] > -1:
                    right = calcPath[r][c+1]
                else:
                    calcPath[r][c+1] = right = dfs(r, c + 1)

            return grid[r][c] + min(down, right)

        return dfs(0, 0)