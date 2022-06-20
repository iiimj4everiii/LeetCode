class Solution:
    def minPathSum(self, grid: list) -> int:

        # Problem:
        # Given a m x n grid filled with non-negative numbers, find a path from top left
        # to bottom right, which minimizes the sum of all numbers along its path.
        # Note: You can only move either down or right at any point in time.

        # Strategy:
        # This is another dynamic programming problem. The idea is that the minimum path
        # sum at any position is equal to the smaller of minimum path sum of its
        # neighbors plus the weight at the current location.
        # However, we need to treat the borders a little differently since they may not
        # have a second neighbor. For the right and bottom border, the path sum for those
        # positions are the cumulative sum from the target position up to the current
        # position. Once solution_table is completely filled out, the minimum path sum
        # from the start position (top left) to the target position (bottom right) is the
        # value at solution_table[0][0]

        # Get the size of grid.
        m = len(grid)
        n = len(grid[0])

        # Create a table of solution of size m x n.
        solution_table = [[0] * n for _ in range(m)]

        # Initialize the path sum at the target location to its own weight.
        solution_table[-1][-1] = grid[-1][-1]

        # At the right border, we can only go down. Therefore, the path sum from those
        # positions are equal to the the path sum of the position right below them plus
        # the weight at the current location.
        for r in reversed(range(m-1)):
            solution_table[r][-1] = solution_table[r+1][-1] + grid[r][-1]

        # At the bottom border, we can only go right. Therefore, the path sum from those
        # positions are equal to the the path sum of the position to their right plus
        # the weight at the current location.
        for c in reversed(range(n-1)):
            solution_table[-1][c] = solution_table[-1][c+1] + grid[-1][c]

        # At every position other than the positions at the right border and at the
        # bottom border,
        for r in reversed(range(m-1)):
            for c in reversed(range(n-1)):

                # the minimum path sum at the current position is equal to the minimum
                # path sum between its' right and downstairs neighbor plus the weight
                # at the current position.
                min_neighbor_path_sum = min(solution_table[r][c+1], solution_table[r+1][c])
                solution_table[r][c] = min_neighbor_path_sum + grid[r][c]

        # Once the entire solution table is filled out, the minimum path sum from upper
        # left corner to bottom right corner is equal to the value at solution_table[0][0]
        return solution_table[0][0]


g = [
    [1,2,3],
    [4,5,6]
]
sol = Solution().minPathSum(g)
print(sol)
