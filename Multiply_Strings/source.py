class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # Motivation:
        # If we need to do multiplication between very large numbers, the
        # product might overflow a 32-bit or 64-bit system. One way to get
        # around this limitation is to use string representation of these
        # numbers.

        # Strategy:
        # We will do multiplication the way we do it by hand (digit by digit).
        # It may be easier to flip the two numbers around and work from left
        # to right instead of right to left.
        # Note #1: notice that the number of digits of the final product never
        # exceeds the combined number of digits of num1 and num2.
        # Note #2: in general, digit in index n multiply by a digit in index m
        # will result in a product in index (n+m).
        # After obtaining the final product, flip the product list, remove the
        # leading zeros, and return the product as a string

        # Handling the corner case.
        if num1 == '0' or num2 == '0':
            return '0'

        # Instead of working from right to left, we will flip
        # num1 and num2 and work from left to right instead.
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Initialize product as a list of size len(num1) + len(num2).
        # Notice that the number of digits in product never exceeds the
        # sum of number of digits of num1 and num2.
        product = [0] * (len(num1) + len(num2))

        # Performing multiplication in the traditional (hand-calculated) way.
        # Notice the pattern: digit in index 0 multiply by another digit
        # in index 0, results in a product in index 0. Similarly, digit in
        # index 1 multiple by a digit in index 0 results in a product in
        # index 1. In general, digit in index n multiply by a digit in index
        # m will result in a product in index (n+m).
        for i in range(len(num1)):
            for j in range(len(num2)):

                # Get the digit-wise product from num1 and num2.
                p = int(num1[i]) * int(num2[j])

                # Add the digit-wise product to the number currently in the
                # same index as this digit-wise product.
                s = product[i+j] + p

                # Assign to this index the ones position of the sum s.
                product[i + j] = s % 10

                # The carry-over (s // 10) is added to the number in the next
                # position (product[i+j+1]).
                c = product[i+j+1] + s // 10

                # Assign to this index the ones position of the carry-over c
                product[i+j+1] = c % 10

                # If carry-over is also overflowing, push it to index (i+j+2).
                # Note that this final carry-over position never overflows.
                if c > 9:
                    product[i+j+2] += c // 10

        # Removing the trailing zeros. This is equivalent to removing the leading
        # zeros when product eventually flips around. We need to do this because
        # our final product needs to be returned as a string.
        while product[-1] == 0:
            product.pop(-1)

        # Flip product around and reformat it as a string.
        res = ''
        for p in reversed(product):
            res += str(p)

        # Return the result of the reformatted product.
        return res


sol = Solution().multiply('0', '1')
print(sol)
