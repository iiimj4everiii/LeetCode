class Solution:

    # # Recursive solution top-down. O(n^2) space
    # def minimumTotal(self, triangle):
    #
    #     # Recursively call itself to get the minimum total from a level below
    #     def get_minimum_total(triangle, row, col):
    #
    #         # Termination condition: return 0 if we go beyond the height of the
    #         # triangle.
    #         if row == len(triangle):
    #             return 0
    #
    #         # Get the minimum total at (row+1, col)
    #         curr_col = get_minimum_total(triangle, row+1, col)
    #
    #         # Get the minimum total at (row+1, col+1)
    #         next_col = get_minimum_total(triangle, row+1, col+1)
    #
    #         # Return the sum of current number and the
    #         # min(minimum total at (row+1, col), minimum total at (row+1, col+1)
    #         return triangle[row][col] + min(curr_col, next_col)
    #
    #     return get_minimum_total(triangle, 0, 0)

    # Dynamic programming solution bottom-up: O(n) space
    def minimumTotal(self, triangle):

        # Get the number of rows/height of the triangle. Notice that we are
        # dealing with an equilateral triangle.
        row_count = len(triangle)

        # Starting from the second to the last row, we work our way up.
        for row in reversed(range(row_count-1)):
            # Starting from the left most index to the right most index in the
            # current row.
            for col in range(row+1):
                # Add to itself the minimum of the two adjacent cells from the
                # row directly below.
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])

        # At this point, the top of the triangle has been updated to the minimum path
        # sum from top to bottom.
        return triangle[0][0]


t = [[2],[3,4],[6,5,7],[4,1,8,3]]
sol = Solution().minimumTotal(t)
print(sol)
