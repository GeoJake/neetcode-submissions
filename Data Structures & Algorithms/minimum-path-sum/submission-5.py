class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        calcPath = [float("inf")] * (COLS+1)

        calcPath[COLS-1] = 0

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                calcPath[c] = grid[r][c] + min(calcPath[c], calcPath[c+1])
        

        return calcPath[0]