class Solution:
    def merge(self, intervals: list) -> list:

        # Strategy:
        # Since we are not sure if intervals will be sorted in any way, we should
        # sort intervals in increasing order by their lower bound (or 0th index).
        # Then we will go through the sorted intervals and see if the current interval
        # overlaps with the next interval. Note that, there are few ways 2 intervals
        # can overlap:
        # 1) (   {   )   }
        # 2) (   {   }   )
        # 3) {   (   }   )
        # 4) {   (   )   }
        # Since intervals are sorted in increasing order by their lower bound, overlaps
        # can only happen in 2 cases (case 1 and case 2). Notice that in both cases, the
        # lower bound of the next interval is smaller than OR EQUAL TO the upper bound of
        # the current interval. When we merge the 2 intervals, we keep the larger upper
        # bound between the 2 intervals.
        # Also, as a consequence of the previous observation, if the next interval DOES NOT
        # overlap with the current interval, any future interval will also not overlap with
        # the current interval. This is because a non-overlap condition happens when the
        # lower bound of the next interval is bigger than the upper bound of the current
        # interval. Any future intervals will have an even higher lower bound. Therefore,
        # when there is no overlap, we update the current interval to the next interval.

        # Sort intervals by their first element.
        intervals = sorted(intervals, key=lambda x: x[0])

        # Initialize solution to an empty list. It may be better to append to solution list
        # rather than popping an interval from the intervals list repeatedly. This is
        # because, POPPING AN ARBITRARY ELEMENT from a list takes O(n) NOT O(1).
        solution = []

        # Initialize current interval index to 0 and the next interval index to 1.
        curr_idx = 0
        next_idx = 1

        # While the next interval index is still within bound, we keep trying to see if
        # the next interval can merge with the current interval.
        while next_idx < len(intervals):

            # Get the current interval and the next interval.
            curr_interval = intervals[curr_idx]
            next_interval = intervals[next_idx]

            # Check to see if the lower bound of the next interval is small than or equal
            # to the upper bound of the current interval. If it is, then we have an overlap.
            if curr_interval[1] >= next_interval[0]:

                # Merge the 2 intervals by keeping the large upper bound between these 2
                # intervals. We already know the lower bound of the current interval is
                # less or equal to the lower bound of the next interval.
                curr_interval[1] = max(curr_interval[1], next_interval[1])

            # If there is no overlap, we append the curr_interval to solutions. Then we move
            # on by setting the current interval to the next interval (or curr_idx to next_idx).
            else:
                solution.append(curr_interval)
                curr_idx = next_idx

            # Continue on with the next interval by incrementing next_idx by 1.
            next_idx += 1

        # Since we do not have a chance to append the last current interval to our solution,
        # we do it one last time outside of our main loop.
        solution.append(intervals[curr_idx])

        return solution


l = []
sol = Solution().merge(l)
print(sol)
