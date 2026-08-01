class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O":
                board[r][c] = "T"
                for dr, dc in d:
                    row = r + dr
                    col = c + dc
                    dfs(row, col)
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1):
                    dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"