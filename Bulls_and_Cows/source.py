class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        # Strategy:
        # 1) Count all the numbers appeared in secret and in guess.
        # 2) Count all the positions where the number in secret is
        #    equal to the number in guess. This is our bull.
        # 3) For each number from 0-9, take the minimum of that
        #    number appears in secret and in guess. This is how many
        #    times this number can be paired up in secret and guess.
        # 4) Sum up all these minimums from 0-9. This number contains
        #    the sum of bulls and cows.
        # 5) To get the number of cows, we simply subtract bull from
        #    this sum.

        num_count = {
            '0':    [0, 0],
            '1':    [0, 0],
            '2':    [0, 0],
            '3':    [0, 0],
            '4':    [0, 0],
            '5':    [0, 0],
            '6':    [0, 0],
            '7':    [0, 0],
            '8':    [0, 0],
            '9':    [0, 0]
        }

        # 1) Count all the numbers appeared in secret and in guess.
        # 2) Count all the positions where the number in secret is
        #    equal to the number in guess. This is our bull.
        bull_count = 0
        for s, g in zip(secret, guess):
            num_count[s][0] += 1
            num_count[g][1] += 1
            if s == g:
                bull_count += 1

        # 3) For each number from 0-9, take the minimum of that
        #    number appears in secret and in guess. This is how many
        #    times this number can be paired up in secret and guess.
        # 4) Sum up all these minimums from 0-9. This number contains
        #    the sum of bulls and cows.
        total_count = 0
        for k in num_count.keys():
            total_count += min(num_count[k])

        # 5) To get the number of cows, we simply subtract bull from
        #    this sum.
        cow_count = total_count - bull_count

        return str(bull_count) + 'A' + str(cow_count) + 'B'


sol = Solution().getHint("01", "10")
print(sol)
