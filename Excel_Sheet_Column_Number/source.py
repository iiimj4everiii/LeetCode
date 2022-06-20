class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        # This is similar algorithm to converting any base to any other base number system
        # In this case, we are using base 26 number system

        sum = 0

        # Loop until we process all the letters in the columnTitle
        for i in range(len(columnTitle)):

            # Get the integer representation of ascii code
            # Notice that we are processing the letters from right to left, not left to right
            number = self.char_to_int(columnTitle[-(i+1)])

            # Add to the sum
            sum += number * 26**i

        return sum

    def char_to_int(self, char):

        # ord() returns the integer representation of an ascii character
        return ord(char) - 64


print(Solution().titleToNumber('AB'))
