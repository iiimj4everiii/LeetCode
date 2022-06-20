class Solution:
    def hammingWeight(self, n: int) -> int:

        #
        # Another weird input format from Leetcode
        #

        # Initialize hamming_weight to 0
        hamming_weight = 0

        # Keep processing n from right to left until n reaches to 0
        while n > 0:

            # Again, (n & 1) expression evaluates to 1 if the rightmost digit is 1.
            # Otherwise, (n & 1) expression will evaluate to 0
            if n & 1:

                # Add to hamming_weight count if we see a 1
                hamming_weight += 1

            # Shift n to the right by 1
            n = n >> 1

        return hamming_weight


print(Solution().hammingWeight(5))
