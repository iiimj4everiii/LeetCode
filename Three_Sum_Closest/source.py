class Solution:
    def threeSumClosest(self, nums, target: int) -> int:

        # Strategy:
        # We will use 2-pointer pattern to heuristically find 2 values at
        # index low and high. These 2 values together with the current value
        # at index 1 will sum to a number that will be close to our target.
        # We will adjust the 2 pointers, low and high, such that we converge
        # towards target:
        # if current sum < target, we move low index up, or else we move the
        # high index down.
        # In order to do this, nums must be sorted.

        # Sort nums and set the diff to be a very large number:
        nums = sorted(nums)
        diff = 2**63 - 1

        # Iterate through nums for the first of the three numbers.
        for i in range(len(nums)):

            # Initialize low to the lowest index > i.
            # Low index will point to the second smallest number next to i
            low = i + 1

            # Initialize high to the highest index in nums.
            # High index will point to the highest number in nums
            high = len(nums) - 1

            while low < high:

                # Get the current three sum
                sum = nums[i] + nums[low] + nums[high]

                # If the absolute diff = abs(target - sum) is smaller than
                # our current abs(diff), then update diff = target - sum
                if abs(target - sum) < abs(diff):
                    diff = target - sum

                # Heuristics:
                # If sum is less than our target, try a bigger number (move
                # the low index up)
                if sum < target:
                    low += 1

                # If sum is greater than our target, try a smaller number
                # (move the high index down)
                elif sum > target:
                    high -= 1

                # Otherwise, we found a three sum that equals to the target
                else:
                    return target

        # Otherwise, return the closest sum = target - diff
        return target - diff


n = [-1,2,1,-4]
print(Solution().threeSumClosest(n, 1))
