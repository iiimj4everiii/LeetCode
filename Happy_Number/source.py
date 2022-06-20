class Solution:
    def isHappy(self, n: int) -> bool:

        # A happy number is a number defined by the following process:
        # 1) Starting with any positive integer,
        #    replace the number by the sum of the squares of its digits.
        # 2) Repeat the process until the number equals 1 (where it will stay),
        #    or it loops endlessly in a cycle which does not include 1.
        # 3) Those numbers for which this process ends in 1 are happy.

        # Create a visited set to detect endless cycle
        visited = set()
        while True:

            # Replace the number by the sum of the squares of its digits
            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n = n // 10

            # If sum already existed in visited set, then we have an endless cycle.
            if sum in visited:
                return False

            # See if sum equals to 1. If it is, then the initial n was a happy number.
            if sum == 1:
                return True

            visited.add(sum)

            # Otherwise, repeat the process by updating n to equal sum
            n = sum


print(Solution().isHappy(3))