class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            dup = set()
            for col in row:
                if not col in dup and col != ".":
                    dup.add(col)
                elif col != ".":
                    return False
        
        for col in range(9):
            dup = set()
            for row in range(9):
                val = board[row][col]
                if not val in dup and val != ".":
                    dup.add(val)
                elif val != ".":
                    return False

        for row in range(0, 6, 3):
            for col in range(0, 6, 3):
                dup = set()
                for i in range(3):
                    for j in range(3):
                        val = board[row + i][col + j]
                        if not val in dup and val != ".":
                            dup.add(val)
                        elif val != ".":
                            return False

        return True