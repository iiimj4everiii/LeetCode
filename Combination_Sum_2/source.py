class Solution:

    # solution: a SET to hold all the combination sum in tuples.
    # Notice that we are using a set here instead of a list as in
    # in the previous problem.
    solution = set()

    def combinationSum2(self, candidates: list, target: int) -> list:

        # For some reason, Leetcode keeps the previous test's solution...
        # So we reset self.solution to an empty set.
        self.solution.clear()

        # Since this algorithm is going to be O(n^2), it will be worth it
        # to sort the candidates and use this relationship to help us.
        candidates.sort()

        # Calling the main worker function to get all the combination sums.
        self.get_combo_sums(candidates, [], target, 0)

        # Since self.solution is a set of tuples, we need to convert it to
        # a list of lists. Return the formatted version of self.solution.
        return self.formatted_solution()

    # We use recursion to go deeper and change target to the difference
    # between the previous target and the current candidate c.
    def get_combo_sums(self, candidates, partial_sum, target, start_idx):

        # Termination condition: if target equals 0, that means partial_sum
        # contains a list of numbers that sums to the original target.
        if target == 0:
            combo_sum = tuple(partial_sum)
            self.solution.add(combo_sum)
            return

        # At this point, target > 0 and partial_sum contains a list of numbers
        # that partially sums to the original target. Target is the second part
        # of original target. Note that since candidates are sorted, we don't
        # have to search from the beginning every time. We only need to search
        # for candidate c to the right of BUT NOT INCLUDING (different than the
        # previous problem: Combination Sum) the previous index.
        i = start_idx
        while i < len(candidates):

            # Get the current candidate
            c = candidates[i]

            # Get the new target
            new_target = target - c

            # Do recursive call only if new_target is non-negative
            if new_target >= 0:
                partial_sum.append(c)

                # Another big difference between the previous problem and this
                # problem is that this problem cannot reuse candidates. So instead
                # of searching to the right of and including the previous index,
                # we are searching to the right of BUT NOT INCLUDING the previous index.
                self.get_combo_sums(candidates, partial_sum, new_target, i+1)

                # Skip trying to evaluate the next candidate next_c if next_c is the same
                # as the current candidate c.
                i += 1
                while i < len(candidates):
                    next_c = candidates[i]
                    if next_c > c:
                        break

                    i += 1

                partial_sum.pop(-1)

            else:
                break

        return

    # Convert set of tuples to list of lists.
    def formatted_solution(self) -> list:

        # The return list of lists.
        res = []

        # Convert tuples to lists and append them to res.
        for t in self.solution:
            res.append(list(t))

        # Return res.
        return res


c = [2,5,2,1,2]
sol = Solution().combinationSum2(c, 5)
print(sol)
