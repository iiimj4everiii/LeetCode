class Solution:
    def spiralOrder(self, matrix: list) -> list:

        # Strategy:
        # Keep track of how many times we can move in any direction.
        # Notice that if we move horizontally, the vertical movement
        # range decreases by 1 after a completely horizontal movement.
        # Similarly, if we move vertically, the horizontal movement
        # range decreases by 1 after a complete vertical movement.

        # When we want to move to the right, we increase the column
        # index col. If we want to move down, we increase the row
        # index. On the other hand, if we want to move to the left,
        # we decrease col and if we want to move up, we decrease row.

        # Handle the corner cases
        if len(matrix) == 0:
            return []

        # Initialize row count to number of matrix rows
        # and column count to number of matrix columns.
        row_count = len(matrix)
        col_count = len(matrix[0])

        # Initialize solution to an empty list.
        solution = []

        # Initialize column col to -1 and row to 0.
        col = -1
        row = 0

        # We will encode our direction with integers:
        #{
        #   0: moves to the right.
        #   1: moves down.
        #   2: moves to the left.
        #   3: moves up.
        #}
        # Initialize direction to 0 (move to the right).
        direction = 0

        # While we can still move: row_count and col_count are both greater than 0
        while row_count > 0 and col_count > 0:

            # Reset direction to 0 when it reaches the 4.
            # This will cycle direction within [0, 1, 2, 3]
            if direction == 4:
                direction = 0

            # Move towards the right direction: increase col index.
            if direction == 0:

                for _ in range(col_count):
                    col += 1
                    solution.append(matrix[row][col])

                # Since we scanned the entire row, we decrease the vertical range by 1.
                row_count -= 1

            # Move towards the down direction: increase row index.
            elif direction == 1:

                for _ in range(row_count):
                    row += 1
                    solution.append(matrix[row][col])

                # Since we scanned the entire column, we decrease the horizontal range by 1.
                col_count -= 1

            # Move towards the left direction: decrease col index.
            elif direction == 2:

                for _ in range(col_count):
                    col -= 1
                    solution.append(matrix[row][col])

                # Since we scanned the entire row, we decrease the vertical range by 1.
                row_count -= 1

            # Move towards the up direction: decrease row index.
            else:

                for _ in range(row_count):
                    row -= 1
                    solution.append(matrix[row][col])

                # Since we scanned the entire column, we decrease the horizontal range by 1.
                col_count -= 1

            # Change the movement direction.
            direction += 1

        return solution


m = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
]
sol = Solution().spiralOrder(m)
print(sol)
