class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Automatically false if x is a negative number: -1 =/= 1-
        if x < 0:
            return False

        # Use our reverse function to reverse the integer
        reverse_x = self.reverse(x)

        # Return true if x is equal to reverse_x
        return x == reverse_x

    # A modified version of reverse from Reverse_Integer source.
    def reverse(self, x: int) -> int:

        # Pop the last digit and append to reverse_int
        reverse_int = 0
        while not x == 0:

            # Extract the last digit by using modulus
            last_digit = x % 10

            # Reduce x by a factor of 10. We are only interested in the integer portion of the reduced x
            # x = int(x / 10)
            x = x // 10     # // is integer division in python

            # Append the extracted last digit to reverse_int
            reverse_int = reverse_int * 10 + last_digit

        # Return the valid reverse_int with the original polarity sign
        return reverse_int


print(Solution().isPalindrome(1234321))
