class Solution:

    # Keeps a memo dictionary for memoization. We want to store previously
    # generated parenthesis for later use. The current set of parentheses will
    # be based on previous parentheses.
    memo = {}

    def generateParenthesis(self, n: int):

        # Strategy:
        # Notice that there is a pattern. The current level's set is generated from 2 subsets:
        # 1) the set that follows the sum pairs pattern (see get_all_sum_pairs() method).
        # 2) the previous level of parenthesis nested within a wrapping parenthesis. e.g.
        # the 4th set of parentheses is generated all the 3rd set of parenthesis nested within a ().
        # Notice that we use a set here in order to remove any duplicates.

        # Handling the corner cases
        if n <= 0:
            return ''

        # Initializing curr_set to '()' and memoize it.
        curr_set = set()
        curr_set.add('()')
        self.memo[1] = curr_set

        # We keep looping until we get to level n number of parentheses per "element"
        for i in range(2, n+1):

            # Re-initialize a new curr_set
            curr_set = set()

            # Get all the sum pairs of i
            sum_pairs = self.get_all_sum_pairs(i)

            # Subset 1:
            # For each pair in sum_pairs, get its left and right counting number that sums to i
            for pair in sum_pairs:

                left = pair[0]
                right = pair[1]

                # Get the generated parentheses in left level left and also in right level from memo
                left_set = self.memo[left]
                right_set = self.memo[right]

                # Get all the combinations of parentheses from the parens in left_set and
                # the parens in right_set.
                for ls in left_set:
                    for rs in right_set:
                        curr_set.add(ls + rs)

            # Subset 2:
            # For each "element" of parentheses set in the previous level, wrap it with a parenthesis ().
            # Then add it to curr_set
            prev_set = self.memo[i-1]
            for paren in prev_set:
                curr_set.add('(' + paren + ')')

            # Memoize the current set for future use.
            self.memo[i] = curr_set

        return list(self.memo[n])

    # Get all pairs of counting numbers that sums to m.
    # e.g. if m = 4, then the list of pairs will be [(1,3), (2,2), (3,1)]
    def get_all_sum_pairs(self, m: int):

        res = []
        for i in range(1, m):
            res.append((i, m-i))

        return res


print(Solution().generateParenthesis(4))
