class Solution:

    # Definition of digit to letters mapping
    digit_to_letters = {
        '2':    ['a', 'b', 'c'],
        '3':    ['d', 'e', 'f'],
        '4':    ['g', 'h', 'i'],
        '5':    ['j', 'k', 'l'],
        '6':    ['m', 'n', 'o'],
        '7':    ['p', 'q', 'r', 's'],
        '8':    ['t', 'u', 'v'],
        '9':    ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str):

        # Strategy:
        # Since we only have 4 different cases, we will deal with it case by case.
        # Case 1: 1 digit. n-Choose-1 where n are the letters mapped to digit
        # Case 2: 2 digits. n-Choose-2 where n are the letters mapped to digit indexed at 0, and 1
        # Case 3: 3 digits. n-Choose-3 where n are the letters mapped to digit indexed at 0, 1, and 2
        # Case 4: 4 digits. n-Choose-4 where n are the letters mapped to digit indexed at 0, 1, 2, and 3
        # We handle the res.append a little different based on the length of digits.

        res = []
        if len(digits) > 0:
            for i in self.digit_to_letters[digits[0]]:
                if len(digits) == 1:
                    res.append(i)
                else:
                    for j in self.digit_to_letters[digits[1]]:
                        if len(digits) == 2:
                            res.append(i + j)
                        else:
                            for k in self.digit_to_letters[digits[2]]:
                                if len(digits) == 3:
                                    res.append(i + j + k)
                                else:
                                    for l in self.digit_to_letters[digits[3]]:
                                        if len(digits) == 4:
                                            res.append(i + j + k + l)
                                        else:
                                            print("Invalid input")

        return res


num = "23"
print(Solution().letterCombinations(num))
