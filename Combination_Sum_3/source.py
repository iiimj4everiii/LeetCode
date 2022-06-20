class Solution:
    def combinationSum3(self, k: int, n: int) -> list:

        # We are going to restrict each of our combinations to a
        # list of integers in increasing order such that their
        # sum equals to n.

        # Precomputed dictionary that tells us the maximum sum we
        # can achieve with k distinct integers.
        upper = {
            1: 9,
            2: 17,
            3: 24,
            4: 30,
            5: 35,
            6: 39,
            7: 42,
            8: 44,
            9: 45
        }

        def get_combo_sum(k, n, start, upper, curr, res):

            # Base case: when k is down to 1, we check to see if n
            # is in-between start and 9 inclusive.
            if k == 1:
                if start <= n <= 9:
                    curr.append(n)
                    res.append(list(curr))
                    curr.pop(-1)
                return

            # If we want to calculate partial sum from a_i to a_j where
            # 1 < 2 < ... < l < a_i < ... < a_l+k = r < ... < 8 < 9,
            # then we calculate the partial sum from 1 to r and
            # subtract from it the partial sum from 1 to l. This is
            # equal to r * (r + 1) // 2 - l * (l + 1) // 2. This number
            # will tell us the minimum sum we can get from adding
            # a_i + a_i+1 + ... + a_l+k-1 + a_l+k. The maximum sum are
            # stored in the upper dictionary.
            l = start - 1
            r = l + k
            minimum = r * (r + 1) // 2 - l * (l + 1) // 2
            maximum = upper[k]

            # If n is smaller than minimum or bigger than maximum, then
            # there is no way to can come up with k distinct integers
            # that can sum up n. Therefore just return.
            if n < minimum or n > maximum:
                return

            # Initialize prev_res_count to the res count before going
            # into the for loop. Also initialize s_large_enough to False.
            prev_res_count = len(res)
            s_large_enough = False

            # try all s from start to 11-k.
            for s in range(start, 11-k):

                # Add s to our current combination.
                curr.append(s)

                # Recursively call get_combo_sum() that finds the combo
                # for n-s using k-1 distinct integers.
                get_combo_sum(k-1, n-s, s+1, upper, curr, res)

                # Pop s out after exploring it.
                curr.pop(-1)

                # If the res size grew, that means s is large enough to
                # partake in summing k distinct integers to n. We set the
                # s_large_enough flag to True.
                if len(res) > prev_res_count:
                    s_large_enough = True

                # We look for s such that it is too large to partake in
                # summing to n. If that is the case, return to the caller.
                # We know that s is too large when the s_large_enough flag
                # is on and res size did not grow (same as previous attempt).
                if s_large_enough and prev_res_count == len(res):
                    return

                # Update prev_res_count to current res size.
                prev_res_count = len(res)

        # Initialize res to an empty list.
        res = []

        # Get the combination sum.
        get_combo_sum(k, n, 1, upper, [], res)

        return res


sol = Solution().combinationSum3(7, 35)
print(sol)
