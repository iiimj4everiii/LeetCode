class Solution:
    def missingNumber(self, nums) -> int:

        # Given an array nums containing n distinct numbers in the range [0, n],
        # return the only number in the range that is missing from the array.

        # Strategy:
        # We find the sum from numbers 0 to n. We can use the partial sum formula:
        # total = n * (n + 1) / 2
        # Then we will subtract all the numbers in nums from the total
        # and what we are left with at the end is the missing number

        # Get n and calculate the partial sum/total
        n = len(nums)
        total = n * (n + 1) // 2

        # Subtract all the numbers in nums from the total
        for num in nums:
            total -= num

        # Return whatever is left in the sum/total
        return total


nums = [3, 0, 1]
print(Solution().missingNumber(nums))
