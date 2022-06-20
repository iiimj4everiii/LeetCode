class Solution:
    def isUgly(self, n: int) -> bool:

        # An ugly number is a positive integer whose prime factors are
        # limited to 2, 3, and 5

        # Since n is a POSITIVE number, we don't have to worry about n = 0
        # However, somehow one of the test cases from leetcode is 0. >_<

        # 1 is not an ugly number. However, somehow Leetcode considers 1 an ugly number.

        # This is not a question. The strategy is:
        # Strategy:
        # Remove all the factors of 2, 3, 5 from n
        # If we are left with n = 1 at the end, that means n's only factors are
        # 2, 3, and/or 5. If we are left with n != 1, that means there are other
        # prime factors in n that is not 2, 3, and/or 5

        # Removing all the 2 factors from n
        while n % 2 == 0:
            n = n / 2

        # Removing all the 3 factors from n
        while n % 3 == 0:
            n = n / 3

        # Removing all the 5 factors from n
        while n % 5 == 0:
            n = n / 5

        # See if we are only left with n = 1
        return n == 1


print(Solution().isUgly(8))
