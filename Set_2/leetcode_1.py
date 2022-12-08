# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.


# We may make the following moves:

# 'U' moves our position up one row, if the position exists on the board;
# 'D' moves our position down one row, if the position exists on the board;
# 'L' moves our position left one column, if the position exists on the board;
# 'R' moves our position right one column, if the position exists on the board;
# '!' adds the character board[r][c] at our current position (r, c) to the answer.
# (Here, the only positions that exist on the board are positions with letters on them.)

# Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

from time import time

a = time()


class Solution:
    def compute(self, board, target):
        for letter in target:
            yield board.index(letter)

    def alphabetBoardPath(self, target: str) -> str:

        self.board = "abcdefghijklmnopqrstuvwxyz"
        self.tar = target
        # x = ["R", "L"]
        # y = ["D", "U"]
        curr_row = 0
        curr_col = 0
        sol = ""
        # target_row = 1
        # target_col = 0

        for position in self.compute(self.board, self.tar):
            target_col = position % 5
            target_row = int(position / 5)

            down = 0
            # print("letter: ", letter)
            # print("curr: ", curr_row, curr_col)
            # print("target: ", target_row, target_col)

            if target_row == 5 and curr_col != 0:
                moves_y = 4 - curr_row
                down = 1
            else:
                moves_y = target_row - curr_row

            moves_x = target_col - curr_col

            # print("moves: ", moves_x, moves_y)x\
            if moves_y > 0:
                sol += moves_y * "D"
            else:
                sol += abs(moves_y) * "U"

            if moves_x > 0:
                sol += moves_x * "R"
            else:
                sol += abs(moves_x) * "L"

            if down == 1:
                sol += "D"

            sol += "!"

            curr_row = target_row
            curr_col = target_col

        # print(sol)
        return sol


S = Solution()
S.alphabetBoardPath("leet")

b = time()

print("results in: ", b - a)
