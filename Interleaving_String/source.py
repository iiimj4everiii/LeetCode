class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Strategy:
        # We will use recursion with memoization to reduce the overall time
        # complexity. If we get to the point where we parsed both s1 and s2, then
        # we found a sequence of interleaving that combines s1 and s2 into s3.
        # Otherwise, if we are done parsing one or the other, we can just compare
        # the rest of s1/s2 to the rest of s3. But, if we still need to parse both
        # s1 and s2, we compare the next letter of both s1 and s2 to the next letter
        # of s3. If they are the same, then we advance their index and recurse deeper
        # until we get to one of the termination conditions.

        def get_is_interleave(s1, idx1, s2, idx2, s3, memo) -> bool:

            # If we get to this point, we know that s3 is an interleave of s1 and s2.
            # Otherwise, we would have failed somewhere else.
            if idx1 + idx2 == len(s3):
                return True

            # If we already did the calculation before at this particular (idx1, idx2),
            # state we can just return the previously calculated result.
            if (idx1, idx2) in memo.keys():
                return memo[(idx1, idx2)]

            # If we are already done parsing s1, we just compare the rest of s2 to the
            # rest of s3. If they are the same, then we return True. False, otherwise.
            if idx1 == len(s1):

                memo[(idx1, idx2)] = s2[idx2:] == s3[idx1+idx2:]

                return memo[(idx1, idx2)]

            # Likewise, if we are already done parsing s2, we just compare the rest of
            # s2 to the rest of s3. If they are the same, then we return True. Otherwise,
            # we return false.
            if idx2 == len(s2):

                memo[(idx1, idx2)] = s1[idx1:] == s3[idx1 + idx2:]

                return memo[(idx1, idx2)]

            # If we still need to parse both s1 and s2, we check the next letter in both
            # s1 and s2. If the next letter in s1 matches the next letter in s3, we advance
            # idx1 and recurse deeper. Otherwise, we know s1 at this state will be Falae.
            if s1[idx1] == s3[idx1+idx2]:
                s1_return = get_is_interleave(s1, idx1+1, s2, idx2, s3, memo)
            else:
                s1_return = False

            # If the next letter in s2 matches the next letter in s3, we advance idx2 and
            # recurse deeper. Otherwise, we know s2 at this state will be False.
            if s2[idx2] == s3[idx1+idx2]:
                s2_return = get_is_interleave(s1, idx1, s2, idx2+1, s3, memo)
            else:
                s2_return = False

            # Memoize the return state of s1 or s2. If either if True, then we can get the
            # interleaved state from (idx1, idx2). Otherwise, this state will lead to a
            # deadline.
            memo[(idx1, idx2)] = s1_return or s2_return
            return s1_return or s2_return

        # Corner case: if the string lengths don't add up, we know s3 is
        # definitely not an interleave of s1 and s2.
        if len(s1) + len(s2) != len(s3):
            return False

        # Keeping a memo to avoid wasteful recalculations
        memo = {}

        return get_is_interleave(s1, 0, s2, 0, s3, memo)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
sol = Solution().isInterleave(s1,s2,s3)
print(sol)
