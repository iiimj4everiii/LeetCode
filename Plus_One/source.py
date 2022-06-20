class Solution:
    def plusOne(self, digits):

        digits[-1] += 1
        i = len(digits) - 1
        while i >= 1 and digits[i] == 10:
            digits[i] = 0
            digits[i-1] += 1
            i -= 1

        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)

        return digits


print(Solution().plusOne([1,2,9,9]))
