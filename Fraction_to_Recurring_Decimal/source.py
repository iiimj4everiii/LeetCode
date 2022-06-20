class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        sign = ""
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            sign = "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        whole = numerator // denominator
        remainder = numerator % denominator

        if remainder == 0:
            return str(sign) + str(whole)
        else:
            res = str(sign) + str(whole) + "."

        memo = {}
        position = len(res)
        while remainder > 0:

            numerator = remainder * 10

            if numerator in memo.keys():
                position = memo[numerator]
                res = res[:position] + "(" + res[position:] + ")"
                break

            memo[numerator] = position
            quotient = numerator // denominator
            remainder = numerator % denominator

            position += 1

            res += str(quotient)

        return res


sol = Solution().fractionToDecimal(2147483647, 37)
print(sol)
