class Solution:

    # solution: a list to hold all the combination sums
    solution = []

    def combinationSum(self, candidates: list, target: int) -> list:

        # For some reason, Leetcode keeps the previous test's solution...
        # So we reset self.solution to an empty list.
        self.solution = []

        # Since this algorithm is going to be O(n^2), it will be worth it
        # to sort the candidates and use this relationship to help us.
        candidates.sort()

        # Calling the main worker function to get all the combination sums.
        self.get_combo_sums(candidates, [], target, 0)

        # Return self.solution that has been updated by the worker function.
        return self.solution

    # We use recursion to go deeper and change target to the difference
    # between the previous target and the current candidate c.
    def get_combo_sums(self, candidates, partial_sum, target, start_idx):

        # Termination condition: if target equals 0, that means partial_sum
        # contains a list of numbers that sums to the original target
        if target == 0:
            combo_sum = list(partial_sum)
            self.solution.append(combo_sum)
            return

        # At this point, target > 0 and partial_sum contains a list of numbers
        # that partially sums to the original target. Target is the second part
        # of original target. Note that since candidates are sorted, we don't
        # have to search from the beginning every time. We only need to search
        # for candidate c to the right of and including the previous index.
        for i in range(start_idx, len(candidates)):

            # Get the current candidate
            c = candidates[i]

            # Get the new target
            new_target = target - c

            # Do recursive call only if new_target is non-negative
            if new_target >= 0:
                partial_sum.append(c)
                self.get_combo_sums(candidates, partial_sum, new_target, i)
                partial_sum.pop(-1)
            else:
                break

        return


c = [1]
sol = Solution().combinationSum(c, 1)
print(sol)
