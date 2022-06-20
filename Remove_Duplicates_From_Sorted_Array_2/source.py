class Solution:
    def removeDuplicates(self, nums: list) -> int:

        # Function to find the next index to swap with.
        def get_swap_index(nums, prev_num, j) -> int:

            # The next index to swap with should contain a number that is
            # strictly greater than prev_num. Current number is the one
            # that will be swapping with the number in this index.
            while j < len(nums):
                if nums[j] <= prev_num:
                    j += 1

                else:
                    return j

            # At this point, we are at the end of nums. Return -1 as an
            # out of bound flag.
            return -1

        # Initialize prev_num to the first number in nums list.
        prev_num = nums[0]

        # At this point, we don't have any duplicate. Initialize
        # duplicate_found to False.
        duplicate_found = False

        # Initialize the current index i and the swapping index j to 1.
        i = 1
        j = 1

        # While the swapping index is still within bound, the current
        # index i will scan through nums.
        while j < len(nums):

            # If the current number is the same as the previous number,
            if nums[i] == prev_num:

                # See if there is already a duplicate. If duplicate_found
                # is False, that means this current number is the second
                # occurrence to prev_num. Set duplicate_found to True.
                if not duplicate_found:
                    duplicate_found = True

                # If duplicate_found is already True, that means this
                # current number is the third occurrence to prev_num. Then
                # we need to find a number to swap with this current number.
                # The next number should be bigger than prev_num. We use our
                # get_swap_index() function to get the swapping index.
                else:
                    j = get_swap_index(nums, prev_num, j)

                    # If the swapping index is still within bound, we swap
                    # these two numbers. Otherwise, nums list is correctly
                    # sorted already. In that case, we just return the
                    # current index i.
                    if j == -1:
                        return i

                    else:
                        nums[i], nums[j] = nums[j], nums[i]

                        # Once we swap these two numbers, we advance j to the
                        # next index and set duplicate_found to False since we
                        # took care of the duplicate concern.
                        j += 1
                        duplicate_found = False

            # If the current number is not the same as prev_num, that means
            # current number is either greater than or smaller than prev_num.
            # If the current number is greater than prev_num, then nums at
            # this point is in a correct state. However,
            else:

                # if the current number is smaller than prev_num, that means
                # we got to this point because we had swapped a smaller
                # number with a larger number previously at this location.
                if nums[i] < prev_num:

                    # If duplicate_found is False, that means this current
                    # position can hold any number greater than or equal to
                    # prev_num. Our current swapping index should hold a
                    # correct value. We swap and advance the swapping index
                    # to the next index.
                    if not duplicate_found:
                        nums[i], nums[j] = nums[j], nums[i]
                        j += 1

                    # If duplicate_found is True, that means this current
                    # position can only hold a value strictly greater than
                    # prev_num. We have to call our get_swap_index() function
                    # as it returns a swapping index that contains a number
                    # strictly greater than prev_num.
                    else:
                        j = get_swap_index(nums, prev_num, j)

                        # If the swapping index is still within bound, we swap
                        # these two numbers. Otherwise, nums list is correctly
                        # sorted already. In that case, we just return the
                        # current index i.
                        if j == -1:
                            return i

                        else:
                            nums[i], nums[j] = nums[j], nums[i]

                            # Once we swap these two numbers, we advance j to the
                            # next index.
                            j += 1

                # Check if there is a duplicate.
                duplicate_found = False
                if nums[i] == prev_num:
                    duplicate_found = True

            # Advance prev_num to our current number
            prev_num = nums[i]

            # Advance the current index i and make sure our swapping index j does
            # not lag behind our current index.
            i += 1
            j = max(i, j)

        return i


# main_nums = [1,1,1,1,2,2,2,3]
# main_nums = [1,1,1,2,2,3]
main_nums = [0,0,1,1,1,1,2,3,3]
# main_nums = [1,1,1,2,2,3,3,3,3]
# main_nums = [1]
sol = Solution().removeDuplicates(main_nums)
print(sol)
print(main_nums)
