class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        # Messier implementation: remainder = columnNumber % 26
        # However, this has a problem with remainder = 0 when column number = 26
        # Which means remainder: 1->A, 2->B, ..., 25->Y, 0->Z,
        # Cleaner Implementation: It may be better to rotate everything down by 1
        # This way: remainder: 0->A, 1->B, ..., 24->Y, 25->Z, 0->A, ...

        excel_title = ''

        # Keep processing until the columnNumber reaches 0
        while columnNumber > 0:

            # Getting the remainder of (columnNumber-1) / 26
            remainder = (columnNumber-1) % 26

            # Convert the remainder to ascii char
            char = self.int_to_char(remainder)
            excel_title += char

            # Remove the processed portion of columnNumber (remainder)
            columnNumber -= remainder

            # Shift the the 26-cimal number by 1 to the right
            columnNumber //= 26

        # Return the reversed version of excel_title because we generated
        # the excel_title string backwards (appending instead of prepending)
        return excel_title[::-1]

    def int_to_char(self, number):

        return chr(number + 65)


print(Solution().convertToTitle(1))
