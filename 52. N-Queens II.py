class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        ans1 = []
        ans2 = [0]
        board = [['.'] * n for i in range(n)]
        column = set()
        negative_diagonal = set() # r - c
        positive_diagonal = set() # r + c

        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in board]
                ans1.append(copy)
                ans2[0] += 1
                return
            
            for col in range(n):
                if col in column or row - col in negative_diagonal or row + col in positive_diagonal:
                    continue
                
                board[row][col] = 'Q'
                column.add(col)
                negative_diagonal.add(row - col)
                positive_diagonal.add(row + col)
                backtrack(row + 1)
                column.remove(col)
                negative_diagonal.remove(row - col)
                positive_diagonal.remove(row + col)
                board[row][col] = '.'

            



        backtrack(0)
        return ans2[0]