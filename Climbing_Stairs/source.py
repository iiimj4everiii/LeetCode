class Solution:
    def climbStairs(self, n: int) -> int:
        # The solutions of this problem is the fibonacci sequence
        return self.fibonacci(n)

    def fibonacci(self, x):

        # Only accept position x >= 1
        assert(x >= 1)

        f_2 = 1
        f_1 = 1
        f = 1
        # Calculating the xth fibonacci number
        for i in range(2, x+1):
            f = f_1 + f_2
            f_2 = f_1
            f_1 = f

        return f


print(Solution().climbStairs(5))
