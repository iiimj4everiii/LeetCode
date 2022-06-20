class Solution:
    def searchInsert(self, nums, target: int) -> int:

        low = 0
        high = len(nums) - 1

        # As long as low is strictly less than high
        while low < high:
            mid = (low + high) // 2

            # Found
            if nums[mid] == target:
                return mid

            # If the number we are currently looking at is greater than the target,
            # we search the left hand side
            elif nums[mid] > target:
                high = mid - 1

            # Otherwise, search the right hand side
            else:
                low = mid + 1

        # At this point, we are in-between 2 indices.
        # If the number we are currently looking at is greater than the target,
        # target should take its spot. Otherwise, target is to the right of it.
        if nums[low] >= target:
            return low
        else:
            return low + 1


l = [1]
print(Solution().searchInsert(l, 1))
