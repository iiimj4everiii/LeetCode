class Solution:
    def countPrimes(self, n: int) -> int:
        # Count the number of prime numbers less than a non-negative number n.

        # Handling special cases
        if n < 2:
            return 0

        # Sieve of Eratosthenes method:
        # We will mark prime numbers with -1 flag and non-prime with 0 flag
        # Generate a number line from 0 (for convenience) to n
        nums = list(range(n))

        # We know 0 and 1 are non-prime. So they are set to 0
        nums[0] = 0
        nums[1] = 0

        # From 2 to n, if nums[i] is not non-prime, then it is prime.
        for i in range(2, n):
            if nums[i] != 0:

                # Then mark every multiple of nums[i]
                # (starting from (nums[i] * i) up to n) as non-prime
                j = i
                while i * j < n:
                    nums[i*j] = 0
                    j += 1

                # Marking nums[i] as a prime
                nums[i] = -1

        # Return the prime count (-1 flags)
        return nums.count(-1)


print(Solution().countPrimes(10))
