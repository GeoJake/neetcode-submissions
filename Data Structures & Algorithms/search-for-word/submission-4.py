class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()

        def dfs(subset, r, c, w_i):
            if subset == word:
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or w_i >= len(word) or not board[r][c] == word[w_i]:
                return False
            w_i += 1
            found = False
            for dr, dc in d:
                row = r + dr
                col = c + dc
                if 0 <= r < ROWS and 0 <= c < COLS and not (r,c) in visited:
                    visited.add((r, c))
                    found = found or dfs(subset + board[r][c], row, col, w_i)
                    visited.remove((r, c))
            return found


        for r in range(ROWS):
            for c in range(COLS):
                if dfs("", r, c, 0):
                    return True

        return False