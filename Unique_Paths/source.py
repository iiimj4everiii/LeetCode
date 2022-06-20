class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Problem:
        # A robot is located at the top-left corner of a m x n grid.
        # The robot can only move either down or right at any point in time.
        # The robot is trying to reach the bottom-right corner of the grid.
        # How many possible unique paths are there?

        # Strategy:
        # This is the dynamic programming problem posted in my lecture.
        # The idea is to see that the solution follows a pattern in a table:
        # 1) The number of unique paths at any position x is the sum
        # of unique paths number from x's right neighbor and x's downstairs
        # neighbor.
        # 2) The number of unique paths at any position at the bottom border
        # and the right border are all 1. This is because, from any position
        # at the bottom border, you can only move right and from any position
        # at the right border, you can only move down.
        # 3) We will in the table, with the initial values from the bottom
        # and from the right border, using the idea from 1) until we get to
        # the top left corner (the starting position).

        # Create a table of solution of size m x n.
        solution_table = [[1] * n for _ in range(m)]

        # From step 2), we want to initialize all the positions at the bottom
        # border and the right border to 1.
        for r in range(m-1):
            solution_table[r][-1] = 1

        for c in range(n-1):
            solution_table[-1][c] = 1

        # We will fill in the rest of the table using the idea from step 1):
        for r in reversed(range(m-1)):
            for c in reversed(range(n-1)):
                # The number of unique paths at any position x is the sum of
                # unique paths number from x's right neighbor and x's downstairs
                # neighbor.
                solution_table[r][c] = solution_table[r][c+1] + solution_table[r+1][c]

        # Return the solution at the top left corner.
        return solution_table[0][0]


sol = Solution().uniquePaths(0,0)
print(sol)
