class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:

        # Problem:
        # A robot is located at the top-left corner of a m x n grid.
        # The robot can only move either down or right at any point in time.
        # The robot is trying to reach the bottom-right corner of the grid.
        # Now consider if some obstacles are added to the grids. How many
        # unique paths would there be?
        # An obstacle and space is marked as 1 and 0 respectively in the grid.

        # Strategy:
        # This is another dynamic programming problem posted in my lecture.
        # The strategy will be similar to the previous problem: Unique_Paths.
        # The only extra thing to keep in mind is that at an obstacle position,
        # there is no way to get to the target position. So this obstacle
        # position will have a value of 0 in the solution_table, rather than
        # the sum of its' right and bottom neighbors.

        # Create a table of solution of size m x n.
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # Instead of initializing borders to 1, we initialize to 0 this time.
        # This is because obstacles at the borders needed to be dealt with
        # separately.
        solution_table = [[0] * n for _ in range(m)]

        # From step 2), we want to initialize all the positions at the bottom
        # border and the right border to 1 until we encounter an obstacle. In
        # that case, we change the initialization value to 0. Since we initialized
        # the entire solution_table to 0, we can simply break out of the loop.
        for r in reversed(range(m)):
            if obstacleGrid[r][-1] == 1:
                break
            solution_table[r][-1] = 1

        for c in reversed(range(n)):
            if obstacleGrid[-1][c] == 1:
                break
            solution_table[-1][c] = 1

        # We will fill in the rest of the table using the idea from step 1):
        for r in reversed(range(m - 1)):
            for c in reversed(range(n - 1)):

                # However, if we encounter an obstacle instead in position x, we
                # simply set the value in that position to 0.
                if obstacleGrid[r][c] == 1:
                    solution_table[r][c] = 0

                # Otherwise, the number of unique paths at any position x is the sum of
                # sum of unique paths number from x's right neighbor and x's downstairs
                # neighbor.
                else:
                    solution_table[r][c] = solution_table[r][c + 1] + solution_table[r + 1][c]

        # Return the solution at the top left corner.
        return solution_table[0][0]


obs = [
    [0,1],
    [0,0]
]
sol = Solution().uniquePathsWithObstacles(obs)
print(sol)
