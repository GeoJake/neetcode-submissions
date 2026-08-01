from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """

        Edge:
            no rotting fruit
            rotting fruit cannot reach the fresh fruit
            no fruit of any kind

        Want to use BFS to track the expansion of rotting at each minute


        """

        ROWS = len(grid)
        COLS = len(grid[0])
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque([])
        total = 0
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] != 0:
                    total += 1
        
        minutes = -1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in d:
                    row = r + dr
                    col = c + dc
                    if 0 <= row < ROWS and 0 <= col < COLS and not (row, col) in visit and grid[row][col] == 1:
                        grid[row][col] = 2
                        visit.add((row, col))
                        q.append((row, col))
                visit.add((r, c))
            minutes += 1 
        
        if not total:
            return 0

        return minutes if total == len(visit) else -1