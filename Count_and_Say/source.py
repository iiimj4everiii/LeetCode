class Solution:
    def countAndSay(self, n: int) -> str:

        # Not sure what kind of application would need a function like this.

        # Strategy:
        # Start with the base case: curr_num = '1'. Set the first digit
        # to curr_s and go through each subsequent digit s. Count until
        # we get to a digit with a different number. Convert the count
        # (curr_s_count) to string, append to it the current number
        # (curr_s), and append both to next_num. We assign curr_s to the
        # new number and begin counting again. Finally, we finish up by
        # appending the last count and the last number to next_num. The
        # next_num will become our new num (curr_num) for the next iteration.
        # We do all this for n-1 number of iterations

        # Initial curr_num to the base case: curr_num = '1'
        curr_num = '1'

        # Do the following for n-1 number of iterations.
        for _ in range(1, n):

            # Initialize next_num to empty string, curr digit number (curr_s)
            # to the first digit number and set count for the current digit
            # number to 1.
            next_num = ''
            curr_s = curr_num[0]
            curr_s_count = 1

            # Go through each subsequent digit and count until we get to
            # a digit with a different number.
            for s in curr_num[1:]:

                if s != curr_s:
                    # Convert the count (curr_s_count) to string, append to it
                    # the current number (curr_s), and append both to next_num.
                    # We assign curr_s to the new number and begin counting again.
                    next_num += str(curr_s_count) + str(curr_s)
                    curr_s = s
                    curr_s_count = 1

                else:
                    curr_s_count += 1

            # Finally, we finish up by appending the last count and the last number
            # to next_num. The next_num will become our new num (curr_num) for the
            # next iteration.
            next_num += str(curr_s_count) + curr_s
            curr_num = next_num

        return curr_num


print(Solution().countAndSay(4))
