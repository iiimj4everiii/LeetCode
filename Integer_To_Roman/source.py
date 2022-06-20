class Solution:

    # Lookup table for decimal to Roman Numeral symbols
    # Format: (Decimal, Roman, Stackable?)
    roman_lut = [
        (1,     'I',    True),
        (4,     'IV',   False),
        (5,     'V',    False),
        (9,     'IX',   False),
        (10,    'X',    True),
        (40,    'XL',   False),
        (50,    'L',    False),
        (90,    'XC',   False),
        (100,   'C',    True),
        (400,   'CD',   False),
        (500,   'D',    False),
        (900,   'CM',   False),
        (1000,  'M',    True)
    ]

    def intToRoman(self, num: int) -> str:

        # Strategy:
        # Chip away num little by little, until num = 0, in Roman Numeral intervals.
        # Starting from the largest Roman Numeral representation, see if we can remove
        # this Roman Numeral value from num. Remove from num if possible and append the
        # Roman Numeral string to return variable roman. If we cannot remove the Roman
        # Numeral value from num, try a lower Roman Numeral representation.

        # Initialize return variable roman and the starting idx of roman_lut (from the end)
        roman = ''
        idx = len(self.roman_lut) - 1

        # If num is nonzero, keep processing num.
        while num > 0:

            # If we can remove Roman Numeral value from num, do that and
            # append Roman Numeral string to roman (the return string)
            if self.roman_lut[idx][0] <= num:
                num -= self.roman_lut[idx][0]
                roman += self.roman_lut[idx][1]

                # Some Roman Numeral symbols are not stackable. If this symbol is not stackable,
                # move on to the next (lower) symbol in the roman_lut
                if not self.roman_lut[idx][2]:
                    idx -= 1

            # If we cannot remove Roman Numeral value from num, then try a lower
            # Roman Numeral representation.
            else:
                idx -= 1

        return roman


print(Solution().intToRoman(3))
