class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:

        # Problem:
        # Write an efficient algorithm that searches for a value in
        # an m x n matrix. This matrix has the following properties:
        # -Integers in each row are sorted from left to right.
        # -The first integer of each row is greater than the last
        #  integer of the previous row.

        # Strategy:
        # Double binary search. Since matrix is sorted in an
        # increasing order from left to right and from top to bottom.
        # We can binary search target row-wise to find the row that
        # target might be in. Then we binary search target
        # column-wise to find the column that target might be in.
        # Return true if matrix[row][column] is the target.
        # False, otherwise.

        # A binary search function for 2D lists.
        def binary_search_2d(matrix, left, right, cond) -> int:

            while left < right:
                mid = (left + right) // 2
                if cond(matrix, mid, target):
                    left = mid + 1
                else:
                    right = mid

            return left

        # Get the matrix size.
        m = len(matrix)
        n = len(matrix[0])

        # Binary search target in the last column.
        left = 0
        right = m - 1
        r = binary_search_2d(matrix, left, right, lambda mat, mid, target: mat[mid][-1] < target)

        # Once we have found the row to search in, we binary search target
        # within the entries of this row.
        left = 0
        right = n - 1
        c = binary_search_2d(matrix, left, right, lambda mat, mid, target: mat[r][mid] < target)

        # Once we have found the column, we return true if matrix[row][column]
        # is our target. False, otherwise.
        return matrix[r][c] == target


m = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
sol = Solution().searchMatrix(m, 20)
print(sol)
