class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        calcPath = [[float("inf")] * (COLS+1) for _ in range(ROWS+1)]

        calcPath[ROWS-1][COLS] = 0

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                calcPath[r][c] = grid[r][c] + min(calcPath[r+1][c], calcPath[r][c+1])
        

        return calcPath[0][0]