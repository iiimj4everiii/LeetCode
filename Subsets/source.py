class Solution:
    def subsets(self, nums: list) -> list:

        # Problem: Given an integer array nums of unique elements, return all
        # possible subsets (the power set).
        # The solution set must not contain duplicate subsets. Return the
        # solution in any order.

        # Strategy:
        # Notice that all possible subsets or the power set is a list of all
        # k combinations of nums where k = 0 to len(nums) inclusive. Since we
        # already have a function (solution to Combinations problem) to get any
        # k combinations, we will use it to solve this problem.

        # Initialize solution list to an empty list.
        solution = []

        # Get all the combinations for k = 0 to len(nums) inclusive. K = 0
        # will give us the empty set, which is a subset of all sets.
        for k in range(len(nums)+1):

            # Extend our solution list to all k combinations.
            solution.extend(self.combine(nums, k))

        # At this point, solution should contain all the subsets of the set
        # nums. Return our solution list.
        return solution

    # A modified version of combine from previous problem: Combinations
    def combine(self, nums: list, k: int) -> list:

        # Our main work function. A recursive function that calls itself
        # to get all the k combinations from nums list starting from start_idx.
        def get_combination(nums, combinations, combo_so_far, start_idx, k) -> None:

            # Termination condition. If k = 0, we don't choose anything
            # from nums. Just append the current combination (combo_so_far)
            # to combinations list and return.
            # Notice that we created a new list with an initial value
            # contained in combo_so_far. Otherwise, we would be appending a
            # reference to combinations instead of a list.
            if k == 0:
                combinations.append(list(combo_so_far))
                return None

            # From start_idx to len(nums)-k+1,
            for idx in range(start_idx, len(nums) - k + 1):
                # we want to append the next choice of number in nums to
                # combo_so_far.
                combo_so_far.append(nums[idx])

                # Get the combinations of k-1 choices from nums list starting
                # from index idx+1.
                get_combination(nums, combinations, combo_so_far, idx + 1, k - 1)

                # At this point, we have gotten all the combinations with
                # number = nums[idx] at this current position. Pop it from
                # combo_so_far and move on with the next number in nums.
                combo_so_far.pop(-1)

            return None

        # Initialize combinations and combo_so_far to an empty list.
        combinations = []
        combo_so_far = []

        # This is the main function that does most of the work. It
        # recursively calls itself with the updated combo_so_far, the new
        # starting index for nums list, and 1 less number of choice (k-1).
        get_combination(nums, combinations, combo_so_far, 0, k)

        # After all the recursive calls, combinations list should contain
        # all of the k combinations chosen from nums list.
        return combinations


n = [1,2,3]
sol = Solution().subsets(n)
print(sol)
