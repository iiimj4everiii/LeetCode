class Solution:
    def addDigits(self, num: int) -> int:

        # Strategy:
        # While num is not a single digit number, do the following:
        # Initialize digit_sum to hold the sum of the digits to zero
        # Sum all the digits by adding the ones digit of num to the digit_sum
        # and shift num to the right by 1 place

        # While num is not a single digit number
        # (quotient greater than or equal to 1 when dividing by 10)
        while num / 10 >= 1:

            # digit sum keeps track of the sum of the digits
            digit_sum = 0

            # While num is nonzero, we keep on adding its ones digit to digit_sum
            # Then shift num's digits to the right by dividing num by 10 and floors it
            while num > 0:
                digit_sum += num % 10
                num = num // 10

            # The new num is now the sum of its digits (digit_sum)
            num = digit_sum

        return num


print(Solution().addDigits(38))
