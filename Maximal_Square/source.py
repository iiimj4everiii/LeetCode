class Solution:
    def maximalSquare(self, matrix: list) -> int:

        # matrix are filled with 0s and 1s but in string format. We
        # are going to solve this problem using dynamic programming.
        # Therefore, it may be better to convert those entries to
        # integers instead.
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])

        # The pattern for this problem is: Starting from the index
        # (1, 1), take the min of the entry's 3 neighbors: up, left
        # and upper-left. Add 1 to that. Then multiply the entire
        # thing by the value at the current location.
        max_side = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = (min(matrix[i-1][j-1], matrix[i-1][j],
                                matrix[i][j-1]) + 1) * matrix[i][j]

        # Return the maximum number ** 2 in the table/matrix.
        return max(max(x) for x in matrix) ** 2


m = [
    ["0","0","0","1"],
    ["1","1","0","1"],
    ["1","1","1","1"],
    ["0","1","1","1"],
    ["0","1","1","1"]
]
sol = Solution().maximalSquare(m)
print(sol)
