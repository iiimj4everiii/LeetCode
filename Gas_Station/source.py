class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:

        # Strategy:
        # Notice that we can solve this problem using dynamic programming.
        # 1) Calculate the difference between gas and cost.
        # 2) Starting from index = 0, calculate rolling sum as we scan
        #    across (and wrap around if the starting index is not 0) the
        #    difference.
        # 3) If we get a negative, rolling sum, we begin our next starting
        #    index at the index right after the index where we summed to a
        #    negative rolling sum.
        # 4) Keep going until our starting index is out of bound. At this
        #    point, no solution exists. So return -1.
        # 5) However, if we able to keep the rolling sum at least 0 when we
        #    scan (and wrap around) the difference for at least one cycle,
        #    then return that starting point.

        # Initialize starting position to index = 0.
        start_idx = 0

        # As long as our start_idx is still within bound, we keep trying to
        # find a starting index that can solve this gas station problem.
        while start_idx < len(gas):

            # Initialize travel count and rolling sum to 0
            count = 0
            rolling_sum = 0

            # Do this until we break out of the loop or successfully return
            # to main.
            while True:

                # Get the current index
                curr_idx = (start_idx + count) % len(gas)

                # Get the rolling sum up to and including curr_idx
                rolling_sum += gas[curr_idx] - cost[curr_idx]

                # If at any point the rolling sum is negative, we break out
                # of the loop and continue on with the next start_idx
                if rolling_sum < 0:
                    break

                # Otherwise, increment count to move curr_idx to the next
                # index.
                count += 1

                # If the travel count is len(gas), that means we successfully
                # made a trip around the circle without breaking out of the
                # loop (due to negative rolling sum). Return the start_idx
                if count == len(gas):
                    return start_idx

            # If we break out of the loop due to negative rolling sum, we try
            # the next start_idx at (count+1) away from the previous start_idx.
            start_idx += count + 1

        # At this point, start_idx is out of bound. No solution exist in this
        # gas/cost pair. Return -1.
        return -1


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
sol = Solution().canCompleteCircuit(gas, cost)
print(sol)
