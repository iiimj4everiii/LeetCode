class Solution:

    def divide(self, dividend: int, divisor: int) -> int:

        # Strategy (Not straightforward):
        # We will not use the native approach to solve this problem.
        # Instead of continuously subtracting divisor from the dividend,
        # we will many multiples of divisor from the dividend to speed up the process.
        # e.g. 36 / 3. We will create a list of divisor multiples [3, 6, 12, 24] that are
        # less than or equal to the dividend. Subtract those divisors from the dividend instead.
        # In this case, 36 - 24 = 12. We took 24 away from 36. So the partial quotient is 8 because
        # 24 / 3 = 8. To get the partial quotient list, we create a quotient multiples [1, 2, 4, 8].
        # The divisor position 24 aligns with the quotient position 8.

        # Next, we try the next largest divisor. 12 - 12 = 0. The divisor position 12 aligns with
        # the quotient position 4. So the partial quotient for this division is 4.

        # Next, we try the next largest divisor. 6 is not smaller than 0. We try the last largest
        # divisor. 3 is not smaller than 0.

        # Finally, we sum up all the partial quotients 8 + 4 = 12. Our final quotient is 12.

        # If dividend is 0, we just return 0.
        if dividend == 0:
            return 0

        # Get the sign of dividend and if dividend is negative,
        # turn it into positive and keep note of its negative polarity.
        is_positive_dividend = True
        if dividend < 0:
            is_positive_dividend = False
            dividend = -dividend

        # Divisor will not be 0.
        if divisor == 0:
            print("Not a test case")

        # Get the sign of divisor and if divisor is negative,
        # turn it into positive and keep note of its negative polarity.
        is_positive_divisor = True
        if divisor < 0:
            is_positive_divisor = False
            divisor = -divisor

        # At this point, we should have a nonzero quotient.
        # Initialize a list of quotients and a list of divisors growing geometrically.
        geo_quotients = [1]
        geo_divisors = [divisor]

        # Creating divisor and quotient lists that grow geometrically.
        # For the quotients list, a = 1 and r = 2.
        # For the divisor list, a = 3, r = 2.
        # One way to generate these lists is iteratively doubling the previous value for the subsequent values.
        doubling_quotients = 1 + 1
        doubling_divisors = divisor + divisor
        while doubling_divisors <= dividend:

            # Doubling the quotients
            geo_quotients.append(doubling_quotients)
            doubling_quotients = geo_quotients[-1] + geo_quotients[-1]

            # Doubling the divisors
            geo_divisors.append(doubling_divisors)
            doubling_divisors = geo_divisors[-1] + geo_divisors[-1]

        # Initialize quotient to be 0.
        quotient = 0

        # We will use the divisors in geo_divisors list to chip away the dividend.
        # The quotients in the geo_quotients list are the pieces of the whole quotient.
        for d, q in zip(reversed(geo_divisors), reversed(geo_quotients)):

            # If d is smaller than dividend, chip d away from dividend.
            if d <= dividend:

                # Chip away d from dividend.
                dividend -= d

                # Add the partial quotient q to the whole quotient.
                quotient += q

        # If the polarity of dividend and divisor is the same, then quotient is a positive number.
        if is_positive_dividend == is_positive_divisor:
            # Clamping the positive quotient to <= 2^31 - 1
            return min(quotient, 2 ** 31 - 1)

        # Otherwise, quotient is a negative number. # Clamping the negative quotient to <= -2^31
        return -min(quotient, 2 ** 31)


print(Solution().divide(2147483648, -1))
