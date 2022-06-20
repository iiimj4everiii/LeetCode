class Solution:
    def combine(self, n: int, k: int) -> list:

        # Our main work function. A recursive function that calls itself
        # to get all the k combinations from nums list starting from
        # start_idx.
        def get_combination(nums, solution, combo_so_far, start_idx, k) -> None:

            # Termination condition. If k = 0, we don't choose anything
            # from nums. Just append the current combination (combo_so_far)
            # to solution list and return.
            # Notice that we created a new list with an initial value
            # contained in combo_so_far. Otherwise, we would be appending a
            # reference to solution instead of a list.
            if k == 0:
                solution.append(list(combo_so_far))
                return None

            # From start_idx to len(nums)-k+1,
            for idx in range(start_idx, len(nums)-k+1):

                # we want to append the next choice of number in nums to
                # combo_so_far.
                combo_so_far.append(nums[idx])

                # Get the combinations of k-1 choices from nums list starting
                # from index idx+1.
                get_combination(nums, solution, combo_so_far, idx+1, k-1)

                # At this point, we have gotten all the combinations with
                # number = nums[idx] at this current position. Pop it from
                # combo_so_far and move on with the next number in nums.
                combo_so_far.pop(-1)

            return None

        # Create a list of numbers from 1 to n inclusive.
        nums = [x for x in range(1, n+1)]

        # Initialize solution and combo_so_far to an empty list.
        solution = []
        combo_so_far = []

        # This is the main function that does most of the work. It
        # recursively calls itself with the updated combo_so_far, the new
        # starting index for nums list, and 1 less number of choice (k-1).
        get_combination(nums, solution, combo_so_far, 0, k)

        # After all the recursive calls, solution list should contain all
        # the n choose k combinations from a list of 1 to n inclusive.
        return solution


sol = Solution().combine(3, 0)
print(sol)
