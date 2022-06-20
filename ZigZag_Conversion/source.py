class Solution:

    def convert(self, s: str, numRows: int) -> str:

        # Strategy:
        # Build a pattern list that aligns with the string s
        # Notice that the pattern for the zig zag conversion follows a sawtooth pattern -
        # the low of the pattern is the 1st row index and the high of the pattern is
        # the (numRows)th row index.

        # Iterate through the indices of pattern or string s (they align with each other),
        # Find the character list that is mapped to the dictionary key = row index

        # A dictionary to look up the [head node, current row node] given a "row"/index number.
        # This will help us quickly locate the current
        row_to_char_list = {}
        for i in range(numRows):
            row_to_char_list[i] = []

        # Initialize zig zag conversion pattern.
        pattern = [0] * len(s)
        forward = True

        # Get the sawtooth pattern of row index. This will be a numerical representation of our zig zag.
        for i in range(1, len(pattern)):

            if forward:
                pattern[i] = pattern[i-1] + 1

                if pattern[i] == numRows-1:
                    forward = False
            else:
                pattern[i] = pattern[i-1] - 1

                if pattern[i] == 0:
                    forward = True

        # Get the characters in each "row":
        # 1) Get the row number from the pattern
        # 2) Get the char list from the row_to_char_list dictionary
        # 3) Append the char s[i] to the end of that row's char_list
        for i in range(len(s)):
            pi = pattern[i]
            char_list = row_to_char_list[pi]
            char_list.append(s[i])

        # Get the characters from the character lists starting from "row" = 1.
        zigzig_converted_string = ''
        for pi in range(numRows):

            char_list = row_to_char_list[pi]
            for char in char_list:
                zigzig_converted_string += char

        return zigzig_converted_string


print(Solution().convert("PAYPALISHIRING", 3))
