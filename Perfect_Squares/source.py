class Solution:
    # def numSquares(self, n: int) -> int:
    #
    #     # Initialize a list of squares to an empty list.
    #     squares = []
    #
    #     # Initialize memo to an empty dict
    #     memo = {}
    #
    #     # Initialize counting number z to 1 and its square to 1
    #     z = 1
    #     z_squared = 1
    #
    #     # Get all the squares up to and including n. We append those squares
    #     # to the square list for iterating and also keep a memo for fast look
    #     # ups later.
    #     while z_squared <= n:
    #
    #         memo[z_squared] = 1
    #         squares.append(z_squared)
    #
    #         z += 1
    #         z_squared = z * z
    #
    #     return self.get_count(n, squares, memo)
    #
    # def get_count(self, n, squares, memo):
    #
    #     # If n is in the memo, then return it. The value mapped to key n is
    #     # the least number of perfect squares sum to n.
    #     if n in memo.keys():
    #         return memo[n]
    #
    #     # Otherwise, find the min_count by trying out all the squares in the list.
    #     min_count = n
    #     for sq in reversed(squares):
    #         if sq <= n:
    #             min_count = min(min_count, self.get_count(n-sq, squares, memo))
    #
    #     # Update the memo with the newfound n: memo[n] = min_count + 1
    #     memo[n] = min_count + 1
    #
    #     return memo[n]

    def numSquares(self, n: int) -> int:

        from collections import deque

        # Initialize a list of squares to an empty list.
        squares = []

        # Initialize queue to an empty deque. We will use this
        # queue for iterative breadth-first-search.
        queue = deque()

        # Initialize counting number z to 1 and its square to 1
        z = 1
        z_squared = 1

        # Get all the squares up to and including n. We append
        # those squares to the square list for iterating.
        while z_squared <= n:

            squares.append(z_squared)
            queue.append((z_squared, 1))

            z += 1
            z_squared = z * z

        # We will keep a list of already calculated c's.
        seen = set()

        # Iterative breath-first-search.
        while queue:

            # Get the next "node" = (c, level). Notice that at any
            # point of time, level is the minimum number of squares
            # needed to sum to c.
            c, level = queue.popleft()

            # If c is what we are looking for, n, then return level.
            if c == n:
                return level

            # Otherwise, loop through all the sq in squares. Add to
            # the current number c and increment level by 1. Put the
            # sum, sm = c + sq, in seen:set if we did not see this
            # sm before. Otherwise, we can ignore this sq.
            for sq in squares:
                sm = c + sq
                if sm not in seen and sm <= n:
                    seen.add(sm)
                    queue.append((sm, level+1))

        return -1


sol = Solution().numSquares(12)
print(sol)
