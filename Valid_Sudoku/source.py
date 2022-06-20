class Solution:
    def isValidSudoku(self, board) -> bool:

        # Strategy:
        # Our simple strategy is to use a set to keep track of all the numbers we encountered
        # when we go through a row, a column, or a 3x3 block. If we come across a number that
        # we came across before, then we know that the sudoku is invalid.

        # Use a set to check if a number already taken in each row or column or 3x3 block.
        number_set = set()

        # Look for duplicate numbers in each row.
        for r in range(9):

            # Clear the set when we start scanning a new row.
            number_set.clear()
            for c in range(9):

                # If there is a duplicate in this row, we return False.
                if self.duplicate_found(number_set, board[r][c]):
                    return False

        # Look for duplicate numbers in each column.
        for c in range(9):

            # Clear the set when we start scanning a new column.
            number_set.clear()
            for r in range(9):

                # If there is a duplicate in this column, we return False.
                if self.duplicate_found(number_set, board[r][c]):
                    return False

        # Look for duplicate numbers in each 3x3 grid
        for tile_r in range(3):

            # Get the start index and stop index of the rows in the 3x3 block
            r_start_idx = 3 * tile_r
            r_stop_idx = 3 * tile_r + 3

            for tile_c in range(3):

                # Get the start index and stop index of the column in the 3xe block
                c_start_idx = 3 * tile_c
                c_stop_idx = 3 * tile_c + 3

                # Clear the set when we start scanning a new 3x3 block.
                number_set.clear()
                for r in range(r_start_idx, r_stop_idx):
                    for c in range(c_start_idx, c_stop_idx):

                        # If there is a duplicate in this 3x3, we return False.
                        if self.duplicate_found(number_set, board[r][c]):
                            return False

        # If we pass all the above tests, then we consider this sudoku puzzle valid.
        return True

    # Check if num exist in number_set. Return true if num exists in number_set.
    # Otherwise, add the number to number_set, except the "." symbol.
    def duplicate_found(self, number_set, num):

        if num in number_set:
            return True
        if num != '.':
            number_set.add(num)

        return False


# b = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]

b = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(Solution().isValidSudoku(b))


