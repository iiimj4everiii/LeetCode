class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # 0 and negative integers are not powers of 2
        if n < 1:
            return False

        # Keep on dividing n by 2 until we either get to 1 or an odd number greater than 1
        # In the former case, the original n is a power of two
        # In the latter case, n will be caught be n % 2 != 0 test and will return False
        while n > 1:

            # If n is not divisible by 2, then it is definitely not a power of 2
            if n % 2 != 0:
                return False

            # Remove a factor of 2 from n
            n = n / 2

        return True


print(Solution().isPowerOfTwo(64))
