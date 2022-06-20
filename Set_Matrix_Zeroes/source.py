class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Problem:
        # Given an m x n integer matrix matrix, if an element is 0, set its
        # entire row and column to 0's, and return the matrix.

        # Constraints:
        # You must do it in place.
        # You must do it with a constant space.

        # Strategy:
        # This problem can be easily done if we do not have the space constraint.
        # To do this problem with O(1) space constraint, we need to put markers
        # on the first row and first column of the matrix. The best marker to
        # use is one that does not equal to any entries in the matrix. However,
        # for generality, we will not use an non-integer marker. For the moment,
        # we will not touch the first row and the first column. Instead, we will
        # keep track of whether or not we need to zero out the first row and the
        # first column. Other than that, we will mark the border entries with 0
        # if these border entries belong to 0-entry's row or column. After
        # putting all the markers on the borders, we need to start zeroing out the
        # rows and columns. Then, we will proceed to process/zero out other rows.
        # Once we are done processing the rows, we will do the same to the columns.
        # After all the columns are zeroed out, we circle back to zeroing out the
        # first row if we needed to and zeroing out the first column if we needed to.

        # Get the size of the matrix.
        m = len(matrix)
        n = len(matrix[0])

        # The difficulty of this problem is solving it with only O(1) space. If
        # we are not careful, we can end up with discrepancies. This is because
        # we need to solve this problem in 2 steps. The first step might change
        # some of the matrix entries that the second step is depending on. i.e.
        # if there is a 0 on the first row, we need to zero the entire first row
        # out. However, doing so will result in zeroing out the entire matrix
        # after doing step 2. This is because all the zeros in the first row will
        # signal the second step to zero out every columns in the matrix.

        # The trick to solve this problem is to do the first row processing and
        # the first column last. Use a variable each to memorize if we need to
        # zero out the first row and the first column at the end.
        zero_first_row = False
        for c in range(n):
            if matrix[0][c] == 0:
                zero_first_row = True
                break

        zero_first_col = False
        for r in range(m):
            if matrix[r][0] == 0:
                zero_first_col = True
                break

        # Mark the rows and columns that will eventually zeroed out. We put the
        # markers on the first row (top border) for all the columns that will
        # be zeroed out. We also put the markers on the first column for all the
        # rows that will be zeroed out.
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Then we move on to zero out the rest of the rows that have 0's in them.
        # These are marked by 0's in the first column.
        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(1, n):
                    matrix[r][c] = 0

        # We move on to zero out the rest of the columns that have 0's in them.
        # These are marked by 0's in the first row.
        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(1, m):
                    matrix[r][c] = 0

        # We circle back to the first row. If we need to zero out the first row,
        # this is the correct time to do so.
        if zero_first_row:
            for c in range(1, n):
                matrix[0][c] = 0

        # We circle back to the first column. If we need to zero out the first
        # column, this is the correct time to do so.
        if zero_first_col:
            for r in range(1, m):
                matrix[r][0] = 0

        return None


# m = [
#     [0,1,2,0],
#     [3,4,5,2],
#     [1,3,1,5]
# ]
# m = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
# m=[[-4,-2147483648,6,-7,0],
#    [-8,6,-8,-6,0],
#    [2147483647,2,-9,-6,-10]
#    ]
m = [[1,0,3]]
Solution().setZeroes(m)
print(m)
