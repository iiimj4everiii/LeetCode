class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:

        # Strategy:
        # We confine the final search space by looking for rows and columns that cannot contain
        # target. We look for the first column, the last column, the first row, and the last row
        # that the target number is in range of. Then we use binary search again (column-wise search)
        # in the confined space row by row to look for target.

        # Initialize left to 0 and right to be the index of the last column.
        left = 0
        right = len(matrix[0])-1

        # Do binary search to find the LAST COLUMN where target is in within this column's range.
        x_high = self.get_index(matrix, target, left, right, lambda mat, tg, idx: tg > mat[0][idx])
        if target < matrix[0][x_high]:
            x_high -= 1

        # Do binary search to find the FIRST COLUMN where target is in within this column's range.
        x_low = self.get_index(matrix, target, left, right, lambda mat, tg, idx: tg > mat[-1][idx])
        if target > matrix[-1][x_low]:
            x_low += 1

        # If we have the first column to the right of the last column, we have an impossibility.
        # Return False.
        if x_low > x_high:
            return False

        # Initialize top to be 0 and bottom to be the index of the last row.
        top = 0
        bottom = len(matrix) - 1

        # Do binary search to find the LAST ROW where target is in within this row's range.
        y_high = self.get_index(matrix, target, top, bottom, lambda mat, tg, idx: tg > mat[idx][x_low])
        if target < matrix[y_high][x_low]:
            y_high -= 1

        # Do binary search to find the FIRST ROW where target is in within this row's range.
        y_low = self.get_index(matrix, target, top, bottom, lambda mat, tg, idx: tg > mat[idx][x_high])
        if target > matrix[y_low][x_high]:
            y_low += 1

        # If we have the first row below of the last row, we have an impossibility. Return False.
        if y_low > y_high:
            return False

        # At this point, we have found a square region [x_low, x_high] x [y_low, y_high] that might
        # contain the target number. We go through them row by row and perform column-wise binary
        # search for target from column x_low to x_high.
        for row in range(y_low, y_high+1):
            mid = self.get_index(matrix, target, x_low, x_high, lambda mat, tg, idx: tg > mat[row][idx])
            if matrix[row][mid] == target:
                return True

        # If we cannot find target after searching through all the rows, then target does not exist
        # in matrix. Return False.
        return False

    @staticmethod
    # Binary search for the critical crossover index.
    def get_index(matrix, target, left, right, cond):

        while left < right:

            mid = (left + right) // 2
            if cond(matrix, target, mid):
                left = mid + 1
            else:
                right = mid

        return left

m = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]

for i in range(1, 36):
    sol = Solution().searchMatrix(m, i)
    print(i, sol)
