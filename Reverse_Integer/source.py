class Solution:
    def reverse(self, x: int) -> int:

        # Check to see if x is negative. If it is, save the negative sign and treat x as a positive integer
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        # Pop the last digit and append to reverse_int
        reverse_int = 0
        while not x == 0:

            # Extract the last digit by using modulus
            last_digit = x % 10

            # Reduce x by a factor of 10. We are only interested in the integer portion of the reduced x
            # x = int(x / 10)
            x = x // 10  # // is integer division in python 3

            # Append the extracted last digit to reverse_int
            reverse_int = reverse_int * 10 + last_digit

        # Check to see if reverse_int is out of bound of the max 32-bit integer value
        if reverse_int > (2 ** 31 - 1):
            return 0

        # Return the valid reverse_int with the original polarity sign
        return sign * reverse_int


print(Solution().reverse(7463847412))
