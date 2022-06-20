class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        # Strategy:
        # Notice that when we count numbers in binary from
        # left to right, only the positions that are different
        # between left and right in binary undergoes a flip.
        # Also notice that if a position undergoes at least 1
        # flip, the result at that position will be 0 after
        # applying bitwise AND operations. Also also notice
        # that the right-most bit undergoes flip most frequently,
        # the second bit from the right flips second most
        # frequently and so on and so forth. Therefore we only
        # need to figure out how many positions will undergo
        # a flip and turn them into 0's.

        # Count the number of positions that are different
        # between left and right.
        count = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            count += 1

        # Turn those into 0's and return.
        return left << count


sol = Solution().rangeBitwiseAnd(5, 7)
print(sol)
