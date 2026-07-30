from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque([])
        visited = set()

        def add_node(r, c):
            nonlocal queue
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visited:
                return
            else:
                queue.append((r, c))
                visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                add_node(r+1, c)
                add_node(r-1, c)
                add_node(r, c+1)
                add_node(r, c-1)
            dist += 1

