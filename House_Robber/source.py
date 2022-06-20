class Solution:
    def rob(self, nums) -> int:

        # Strategy:
        # We can think of this problem as a decision to either
        # rob the ith house or the (i+1)th house. The problem
        # can be visualized as a binary tree where the root is
        # at the starting position, house #1 is the left node,
        # and house #2 is the right node. If we choose to rob
        # house #1, then we can only rob house #3 or house #4
        # later. However, we can choose to rob house #2 instead,
        # we can only choose to rob house #4 or house #5 later.
        # So we can use recursion to solve this problem. The
        # maximum amount of money we can get is the larger of
        # (robbing the ith house + the maximum amount of money
        # we can rob starting from house i+2) and (robbing the
        # (i+1)th house + the maximum amount of money we can
        # rob starting from house i+3.

        # A function to recursively rob the maximum amount of
        # money in the rest of the list.
        def get_max_rob(nums, i, memo):

            # Termination condition: if we are out of bound,
            # return 0.
            if i >= len(nums):
                return 0

            # Assume we choose to rob house i, then the rest
            # of the houses we can rob are from i+2 to end.
            # Recursively call get_rob to get the max amount
            # of money we can rob from house i+2 to end. left
            # holds the maximum amount of money we can get if
            # we choose to rob house i.
            if i in memo.keys():
                left = memo[i]
            else:
                left = nums[i] + get_max_rob(nums, i + 2, memo)
                memo[i] = left

            # Likewise, we want to see what is the max amount
            # of money we can get if we choose to rob house
            # i+1 instead of i. We do the same as with left:
            # we choose to rob house i+1 and recursively call
            # get_rob to get the max amount of money we can
            # rob from house i+3 to end. right holds the max
            # amount of money we can get if we choose to rob
            # house i+1 instead of i.
            right = 0
            if i + 1 < len(nums):
                if i + 1 in memo.keys():
                    right = memo[i+1]
                else:
                    right = nums[i+1] + get_max_rob(nums, i + 3, memo)
                    memo[i+1] = right

            # Return the max of the two choices.
            return max(left, right)

        # To avoid recalculation, we use a memo to store the
        # calculated maximum amount of money we can get if we
        # start robbing from house i.
        memo = {}
        return get_max_rob(nums, 0, memo)


n = [226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]
sol = Solution().rob(n)
print(sol)
