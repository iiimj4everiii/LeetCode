class Solution(object):
    def nthUglyNumber(self, n):

        # NOT AN EASY PROBLEM TO SOLVE. A LOT OF TWISTS AND TURNS.

        # Strategy:
        # We will generate a list, ans, containing numbers that are
        # only multiples of our ugly multiplier {2, 3, 5}. However,
        # we will not be generating multiples of our ugly multipliers
        # from the integer set because that will eventually take us
        # to a different prime number other than our ugly multipliers.
        # The trick is to take the multiples of the generated list.
        # The numbers will be generated in order so the next multiple
        # will be the next smallest ugly number.

        # Initialize our generated list to 1.
        ans = [1]

        # Initialize the x2, x3 and x5 indices of ans to 0. These
        # indices point to the location of the ugly number in ans that
        # the respective ugly multiplier is currently operating on.
        i2 = 0
        i3 = 0
        i5 = 0

        # We keep generating ugly numbers as long as we have less than
        # k ugly numbers.
        while len(ans) < n:

            # Get each ugly multiplier's next smallest multiple.
            x2 = ans[i2] * 2
            x3 = ans[i3] * 3
            x5 = ans[i5] * 5

            # Out of all of next smallest multiples, get the smallest
            # multiple and append it to ans.
            x = min(x2, x3, x5)
            ans.append(x)

            # Increment the indices, which point to the location of the
            # ugly number in ans, of the multiples that matches the
            # currently smallest multiple x.
            if x2 == x:
                i2 += 1
            if x3 == x:
                i3 += 1
            if x5 == x:
                i5 += 1

        # Return the last ugly number in ans.
        return ans[-1]


sol = Solution().nthUglyNumber(10)
print(sol)
