from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["."] * n for _ in range(n)]
        ans = []

        directions = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (-1, -1), (-1, 1),
            (1, -1), (1, 1)
        ]

        def isSafe(row, col):

            for dx, dy in directions:

                step = 1

                while True:

                    new_row = row + step * dx
                    new_col = col + step * dy

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

                if isSafe(row, col):

                    board[row][col] = "Q"

                    Queen(row + 1)

                    # Backtracking
                    board[row][col] = "."

        Queen(0)

        return ans