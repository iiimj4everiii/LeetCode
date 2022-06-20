class Solution:
    def partition(self, s: str) -> list:

        def do_partition(solution, curr_sol, memo, s, start, stop):

            # Termination condition: if we go out of scope, we know that we
            # have successfully found a valid palindrome partition of s. If
            # not, we would not have gotten to this step because we would
            # have continue on with the next iteration in the for loop.
            # Create a new list initialized with curr_sol, append to our
            # solution list and return.
            if start == stop:
                solution.append(list(curr_sol))
                return

            # Iterate through different partition indices.
            for part_idx in range(start, stop):

                # Get the left side of the partition.
                left = s[start:part_idx+1]

                # Check if left is in the memo. Add left to curr_sol if left
                # is a true palindrome. Otherwise, continue on with the next
                # iteration.
                if left in memo.keys():
                    if memo[left] is True:
                        curr_sol.append(left)
                    else:
                        continue

                # If left is not in the memo, check if left is a palindrome
                # by comparing it with the inverted/reversed left. If left
                # is a palindrome, add left to curr_sol and also note it
                # in the memo.
                else:
                    if left == left[::-1]:
                        curr_sol.append(left)
                        memo[left] = True

                    # If left is not a palindrome, note it in the memo and
                    # continue on with the next iteration.
                    else:
                        memo[left] = False
                        continue

                # At this point, we know left is a valid palindrome. If left
                # is not a palindrome, we would have continue on with the
                # next iteration. Recurse the right side of the partition
                # starting with part_idx+1.
                do_partition(solution, curr_sol, memo, s, part_idx+1, stop)

                # Pop the current left (last appended item) from curr_sol and
                # try a different left/partition_idx in the next iteration.
                curr_sol.pop(-1)

            return

        # Initialize solution to an empty list.
        solution = []

        # Initialize memo to an empty dictionary.
        memo = {}

        # Call do_partition method to get the solution to all the palindrome
        # partitions of s.
        do_partition(solution, [], memo, s, 0, len(s))

        return solution


string = "abcba"
sol = Solution().partition(string)
print(sol)
