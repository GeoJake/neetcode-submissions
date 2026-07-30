from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647

        directions = [[1,0], [0,-1], [0, 1], [-1, 0]]

        def BFS(r, c):
            queue = deque([(r, c)])
            visited = [[False] * COLS for _ in range(ROWS)]
            visited[r][c] = True
            steps = 0
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    if not grid[row][col]:
                        return steps
                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc
                        if r >= 0 and c >= 0 and r < ROWS and c < COLS and grid[r][c] != -1 and not visited[r][c]:
                            visited[r][c] = True
                            queue.append((r, c))
                steps += 1
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = BFS(r, c)