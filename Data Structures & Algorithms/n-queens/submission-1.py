from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for i in range(n)]
        ans = []

        checkPoint=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

        def canPut(row, col):
            for r,c in checkPoint:
                step = 1

                while True:
                    new_row = row + step * r
                    new_col = col + step * c

                    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
                        break

                    if board[new_row][new_col] == "Q":
                        return False

                    step += 1

            return True

        def Queen(row):

            if row == n:
                temp = []
                for r in board:
                    temp.append("".join(r))
                ans.append(temp)
                return

            for col in range(n):
                if canPut(row, col):
                    board[row][col] = "Q"
                    Queen(row + 1)

                    # Backtracking
                    board[row][col] = "."

        Queen(0)
        return ans