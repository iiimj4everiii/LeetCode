class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Since we need to modify board in-place but we also need
        # to look at the untouched board state, we will make a deep
        # copy of board.
        board_copy = [[0 for _ in board[0]] for _ in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                board_copy[i][j] = board[i][j]

        # Go through every position in board, find the number of
        # neighbors in each position and decide the fate of the
        # state of that position based on the rules in Game of Life.
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = self.get_neighbor_count(board_copy, i, j)

                if count < 2 or count > 3:
                    board[i][j] = 0
                elif count == 3:
                    board[i][j] = 1

        return None

    # This method is used to get the neighbor counts at the board
    # position (i, j)
    @staticmethod
    def get_neighbor_count(board, row, col):
        count = 0
        for i in [row-1, row, row+1]:
            for j in [col-1, col, col+1]:

                if i == row and j == col:
                    continue

                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    if board[i][j] == 1:
                        count += 1

        return count


mat = [
    [1,1],
    [1,0]
]
Solution().gameOfLife(mat)
print(mat)
