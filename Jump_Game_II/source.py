class Solution:
    def jump(self, nums: list) -> int:

        # Jump Game II:
        # Given an array of non-negative integers nums, you are initially positioned at
        # the first index of the array.
        # Each element in the array represents your maximum jump length at that position.
        # Your goal is to reach the last index in the minimum number of jumps.
        # You can assume that you can always reach the last index.

        # Strategy:
        # This is a O(n^2) algorithm.
        # Begin by initializing a result list res_list to very large numbers.
        # res_list represents the minimum number of jumps needed to reach the
        # last index at every index/position in the list.
        # Set the last index of res_list to 0 because in this index/position,
        # we don't need to jump to get to the last index/position.
        # For every other index i not including the last index, explore nums[i] indices
        # to the right of nums[i] up to the last index. Recoded the minimum steps needed
        # to get to the last index/position. This can be done by updating
        # res_list[i] = min(1+res_list[j]) for all j from i+1 to the min of:
        # i+1+nums[i] and len(nums)-1.

        res_list = [2 ** 31 - 1] * len(nums)
        res_list[-1] = 0

        # For index i not including the last index,
        for i in reversed(range(len(nums)-1)):
            # explore nums[i] indices to the right of nums[i] up to the last index.
            for j in range(i+1, i+1+nums[i]):

                # Recoded the minimum steps needed to get to the last index/position.
                # This can be done by updating res_list[i] = min(1+res_list[j])
                # for all j from i+1 to i+1+nums[i]
                if 1+res_list[j] < res_list[i]:
                    res_list[i] = 1+res_list[j]

                # If j is already in the last index, break to avoid index out of bound.
                if j == len(nums) - 1:
                    break

        # Return the minimum number of jumps needed to reach the last index at index 0.
        return res_list[0]


n = [2,2,0,1,4]
sol = Solution().jump(n)
print(sol)
