class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or 
                r < 0 or c < 0 or r == ROWS or c == COLS or 
                heights[r][c] < prevHeight):
                return
            
            visit.add((r, c))

            for dr, dc in dir:
                next_R = r + dr
                next_C = c + dc
                dfs(next_R, next_C, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
            
        res = pac.intersection(atl)

        return list(res)