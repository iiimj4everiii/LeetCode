class Solution:
    def reverseBits(self, n: int) -> int:

        #
        # Weird problem with leetcode's input format.
        #

        # Initialize return reversed_bits to 0 and start with power = 31
        reversed_bits = 0
        power = 31

        # While n is non-zero, we keep processing n from right to left
        while n > 0:

            # (n & 1) is 1 if the rightmost digit is 1. 0, otherwise.
            # Then shift (1 or 0) to the left power number of times
            reversed_bits += (n & 1) << power

            # Decrease power by 1
            power -= 1

            # Shift n to the right 1 time
            n = n >> 1

        return reversed_bits
