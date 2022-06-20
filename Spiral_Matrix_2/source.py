class Solution:
    def generateMatrix(self, n: int) -> list:

        # Strategy:
        # Similar strategy as Spiral_Matrix problem. However, instead of
        # getting matrix elements in a clockwise spiral traversal, we want
        # to write to a matrix in an incremental order.

        # We create a function to write to a matrix/solution. This function
        # uses a function pointer to change the matrix/solution indices. This
        # function pointer is passed as a lambda function from the main loop.
        def matrix_write(solution: list, row: int, col: int, write_count: int, spiral_count: int,
                         get_next_index) -> list:

            for _ in range(write_count):

                [row, col] = get_next_index(row, col)
                solution[row][col] = spiral_count

                # Increment count by 1.
                spiral_count += 1

            return [row, col, spiral_count]

        # Initialize row count and column count to n.
        row_count = n
        col_count = n

        # Initialize solution to nxn 2D list. We have to use this code
        # to initialize 2D list. The shorthanded way does not work as intended.
        solution = [[0]*n for _ in range(n)]

        # Just like the previous problem: Spiral_Matrix,
        # we initialize column col to -1 and row to 0.
        col = -1
        row = 0

        # We will encode our direction with integers:
        # {
        #   0: moves to the right.
        #   1: moves down.
        #   2: moves to the left.
        #   3: moves up.
        # }
        # Initialize direction to 0 (move to the right).
        direction = 0

        # spiral_count will keep track of the integer to be written to our solution
        # list at any point. This variable will increment by 1 every time we write
        # to our solution list.
        spiral_count = 1

        # While we can still move: row_count and col_count are both greater than 0
        while row_count > 0 and col_count > 0:

            # Reset direction to 0 when it reaches the 4.
            # This will cycle direction within [0, 1, 2, 3]
            if direction == 4:
                direction = 0

            # Move towards the right direction: increase col index.
            if direction == 0:

                # Write to solution
                [row, col, spiral_count] = matrix_write(solution, row, col, col_count, spiral_count,
                                                        lambda y, x: [y, x + 1])

                # Since we scanned the entire row, we decrease the vertical range by 1.
                row_count -= 1

            # Move towards the down direction: increase row index.
            elif direction == 1:

                # Write to solution
                [row, col, spiral_count] = matrix_write(solution, row, col, row_count, spiral_count,
                                                        lambda y, x: [y + 1, x])

                # Since we scanned the entire column, we decrease the horizontal range by 1.
                col_count -= 1

            # Move towards the left direction: decrease col index.
            elif direction == 2:

                # Write to solution
                [row, col, spiral_count] = matrix_write(solution, row, col, col_count, spiral_count,
                                                        lambda y, x: [y, x - 1])

                # Since we scanned the entire row, we decrease the vertical range by 1.
                row_count -= 1

            # Move towards the up direction: decrease row index.
            else:

                # Write to solution
                [row, col, spiral_count] = matrix_write(solution, row, col, row_count, spiral_count,
                                                        lambda y, x: [y - 1, x])

                # Since we scanned the entire column, we decrease the horizontal range by 1.
                col_count -= 1

            # Change the movement direction.
            direction += 1

        return solution


sol = Solution().generateMatrix(4)
print(sol)
