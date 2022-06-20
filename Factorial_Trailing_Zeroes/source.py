class Solution:
    # def trailingZeroes(self, n: int) -> int:
    #
    #     # Strategy: we count how many 5's can be divided from n!
    #     # All these 5's can be matched with an even number to become 10
    #     # These 10's are what's contributing to the trailing zeros
    #
    #     # Intuitive solution:
    #     # We go from 5 to n and count how many times we can divide i by 5 in steps of 5
    #     # Notice that we are interested in every 5th number in the number line
    #     count = 0
    #     # for i in range(1, n+1):
    #     for i in range(5, n + 1, 5):
    #
    #         # Keep on dividing by 5 if we can
    #         while i % 5 == 0:
    #             count += 1
    #             i /= 5
    #
    #     return count

    def trailingZeroes(self, n: int) -> int:

        # Faster solution:
        # The number of trailing zeroes, is exactly the number of 5's and 2's
        # that are multiplied by each other in the factorial of n.
        # Because 2's happened much more frequently than 5's, we only need to count
        # the number of 5's in the factorial of n.
        # For that we divide n by powers of 5 and add the div to result.

        count = 0
        i = 1

        while True:

            count_at_i = n // (5 ** i)

            if count_at_i == 0:
                return count

            count += count_at_i

            i += 1

