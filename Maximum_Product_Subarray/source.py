class Solution:
    def maxProduct(self, nums) -> int:

        # Explanation:
        # At each value, we simply either take the value or don't take
        # the value. It's very similar to the maximum subarray.

        # At each point, you simply cache a min value and a max value,
        # any min value can be constructed from the num at an index,
        # the products of all mins before and the current num or the max
        # multiplied by the current num if the num is negative.

        # Initialize current maximum to the first element in nums.
        maximum = nums[0]
        min_rolling = nums[0]
        max_rolling = nums[0]

        for n in nums[1:]:

            # Keeps the most negative. We keep this in case most negative
            # can potentially turn into most positive.
            temp_min = min(n, min_rolling * n, max_rolling * n)

            # Keeps the most positive.
            temp_max = max(n, min_rolling * n, max_rolling * n)

            min_rolling = temp_min
            max_rolling = temp_max

            # Update maximum if max_rolling is greater than the current
            # maximum.
            maximum = max(maximum, max_rolling)

        return maximum


n = [-1, 0, -2, 5, -10]
sol = Solution().maxProduct(n)
print(sol)
