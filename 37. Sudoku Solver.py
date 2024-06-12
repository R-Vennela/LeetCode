class Solution:
    def solveSudoku(self, board) :
        def valid_move(r, c, n):
            for i in range(9):
                if board[i][c]==n: return False
                if board[r][i]==n: return False
                if board[3*(r//3)+i//3][3*(c//3)+i%3]==n: return False
            return True
        
        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c]!=".": continue
                    for n in "123456789":
                        if valid_move(r, c, n):
                            board[r][c] = n
                            if backtrack(): return True
                            board[r][c] = "."
                    return False
            return True
        backtrack()