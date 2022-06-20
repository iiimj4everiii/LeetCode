class Solution:
    def permuteUnique(self, nums: list) -> list:

        # Strategy:
        # This algorithm uses recursive call on self.get_permutation() to get
        # the rest of the permutations. We begin by turning nums from a list to a
        # set, nums_set. This is because we will be searching, adding and removing
        # elements from this set. These operations are faster with hashing. Also
        # initialize our current permutation and our final solution to []. Permutation
        # list will dynamically change and hold the current permutation.
        # self.get_permutations will be doing most of the work by recursively calling
        # itself and appending current permutation to our final solution.

        # In this problem, duplicates are allowed in nums. Therefore, we need a way
        # to get the permutations WITHOUT DOING ANY DUPLICATE WORK. We can use the
        # same concept as we did with combination_sum_2 problem:
        # 1) Sort nums and use the sorted relationship to help us skip elements.
        # 2) Skip the current element if the current element is the same as the
        # previous element.

        # Sort nums and use the sorted relationship to help us skip elements.
        nums.sort()

        # Initialize our current permutation and our solution to an empty list.
        solution = []
        permutation = []

        # Call self.get_permutations() to do most of the work.
        self.get_permutations(nums, permutation, solution)

        # Return the solution generated by self.get_permutations().
        return solution

    def get_permutations(self, nums, permutation, solution):

        # The termination condition for self.get_permutation() is when nums_set
        # is empty. At this point, permutation list is ready to be added to our
        # solution list.
        if len(nums) == 0:
            solution.append(list(permutation))
            return

        # Otherwise, we iterate through nums_set, which may be smaller than the
        # original nums_set in size (new_nums_set of the caller). Notice that
        # we are using a while loop instead of a for loop because we may need to
        # skip some elements later on if the next element is the same as this
        # current element.
        i = 0
        while i < len(nums):
            # Otherwise, we create a new nums_set to avoid changing the original
            # nums_set that we are currently iterating through.
            new_nums = list(nums)

            # We remove the element n from new_nums_set and append it to our
            # current permutation list.
            new_nums.pop(i)
            permutation.append(nums[i])

            # Then recursively call self.get_permutations() with new_nums_set,
            # the current permutation list, and our current final solution list.
            self.get_permutations(new_nums, permutation, solution)

            # As we unwind the recursive calls, we pop the last element from
            # our current permutation list.
            permutation.pop(-1)

            i += 1
            # Skip the current element if the current element is the same as the
            # previous element.
            while i < len(nums):

                # If the current element is the same as the previous element, skip.
                if nums[i] == nums[i-1]:
                    i += 1

                # Otherwise, break out of the skipping loop.
                else:
                    break

        return


l = [1,2,3]
sol = Solution().permuteUnique(l)
print(sol)