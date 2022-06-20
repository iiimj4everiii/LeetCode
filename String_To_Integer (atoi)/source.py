class Solution:
    def myAtoi(self, s: str) -> int:

        sign = 1
        num_found = False
        integer = 0

        for char in s:

            # If we find non-numeric after num_found is True, then we break.
            if num_found and not char.isnumeric():
                break

            # Whenever we see an alphabet, we break.
            if char.isalpha():
                break

            # If we encounter a plus sign, ignore it.
            if char == '+':
                continue

            # If we see a negative sign,
            if char == '-':

                # Flip the sign
                if sign == 1:
                    sign = -1
                else:
                    sign = 1

                continue

            # Handling floating point numbers.
            # Break since we can ignore all the numbers following the decimal point.
            if char == '.':
                break

            # If we see a whitespace,
            if char.isspace():
                # ignore it if the whitespaces are leading.
                if not num_found:
                    continue
                # break it if we see a trailing whitespace
                else:
                    break

            # "Append" the int(char) to the integer.
            # This integer will hold the return integer converted from string.
            integer = integer * 10 + int(char)
            num_found = True

        # Return the clamped integer.
        return self.clamp(sign * integer, -2**31, 2**31 - 1)

    def clamp(self, num, min_num, max_num):

        return min(max(min_num, num), max_num)


print(Solution().myAtoi('-91283472332'))
