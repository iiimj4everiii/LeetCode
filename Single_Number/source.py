class Solution:
    def singleNumber(self, nums):

        # Keeping a set of numbers that we see for the first time
        nums_set = set()

        for n in nums:
            # If n is already in the set, we have already seen it
            if n in nums_set:
                # Then, we can remove it from the set
                nums_set.remove(n)

            # Otherwise, we add the number to the set
            else:
                nums_set.add(n)

        # Return the only number left in the set
        return nums_set.pop()


nums = [2,2,1]
print(Solution().singleNumber(nums))
