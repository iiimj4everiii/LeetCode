from collections import deque

class Solution:
    def maxSubArray(self, nums) -> int:

        # Handling a corner case.
        if len(nums) == 0:
            return 0

        # If there is at least one positive number
        if positive_in_list(nums):

            # Simplify the list by combining (adding) numbers with the same sign.
            for i in reversed(range(len(nums)-1)):
                prev_n = nums[i+1]
                if sign(prev_n) == sign(nums[i]) or nums[i] == 0:
                    nums[i] = nums[i] + nums.pop(i+1)

            # At this point, we should have an alternating pattern of positive and negative integers.
            # We remove the negative numbers on the edges.
            if nums[0] <= 0:
                nums.pop(0)

            if nums[-1] <= 0:
                nums.pop(-1)

            max_so_far = max(nums)

            # Combine 3 neighboring numbers if the abs(both edge numbers) are greater than the center number.
            # Finished where there are no more updates.
            updated = True
            while len(nums) > 2 and updated:

                i = 0
                updated = False

                while i < len(nums)-2:
                    if abs(nums[i]) >= abs(nums[i+1]) and abs(nums[i+2]) >= abs(nums[i+1]):
                        nums[i] = nums[i] + nums.pop(i+2)
                        nums[i] = nums[i] + nums.pop(i+1)

                        max_so_far = max(max(nums), max_so_far)
                        updated = True
                    else:
                        i = i + 1

            return max_so_far

        else:

            return max(nums)


def sign(num):
    if num < 0:
        return -1
    return 1


def positive_in_list(nums):
    for n in nums:
        if n > 0:
            return True
    return False


l = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(l))
