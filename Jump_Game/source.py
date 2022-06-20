class Solution:
    def canJump(self, nums: list) -> bool:

        # Problem:
        # You are given an integer array nums. You are initially positioned at the
        # array's first index, and each element in the array represents your maximum
        # jump length at that position. Return true if you can reach the last index,
        # or false otherwise.

        # Strategy:
        # We try to see if we can get to the last/destination index from any position
        # to the left of the last/destination index. If we can, then update the
        # last/destination index to this new position/index. Then continue to scan
        # left of nums to see if we can get to this new destination index from any
        # position to the left of this new destination index. If we can, then update
        # the destination index and repeat.
        # At the end, if destination_index is at the 0th index, that means we can
        # get to the last index from the 0th index (first position of nums).

        # Set the destination_index to the last index of nums.
        destination_index = len(nums)-1

        # Start from the second to the last index of nums (we can also start from
        # the last index), see if we can get to destination_index from any
        # position/index before it. If we can, update the destination index to
        # this new position/index.
        for i in reversed(range(len(nums)-1)):
            if nums[i] >= destination_index-i:
                destination_index = i

        # If the destination_index can be moved to the 0th index, this means that
        # we can get to the original destination index (the last index of nums) from
        # the 0th index (or the first position of nums)
        return destination_index == 0


l = [2,3,1,0,4]
sol = Solution().canJump(l)
print(sol)
