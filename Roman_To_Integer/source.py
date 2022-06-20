class Solution:
    def romanToInt(self, s: str) -> int:

        # Get the Roman to Integer look up table
        roman_dict = self.roman_table()

        roman_int = 0
        prev_value = 0
        for s_i in s:
            current_value = roman_dict[s_i]

            # If everything is normal, we just add the new value to roman_int
            if current_value <= prev_value:
                roman_int = roman_int + current_value
            else:
                # If the current value is bigger than the previous value,
                # we need to subtract the previous value, not add the previous value
                roman_int = roman_int - 2 * prev_value + current_value

            # Set the prev_value to the current value
            prev_value = current_value

        return roman_int

    def roman_table(self) -> dict:
        roman_LUT = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        return roman_LUT


print(Solution().romanToInt("MCMXCIV"))
