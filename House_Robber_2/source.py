class Solution:
    def rob(self, nums: list) -> int:

        def get_max_rob(nums, i, memo):

            # Base case: if index i is in an invalid position:
            # 1) Out of bound.
            # 2) Last home neighboring first home.
            if i >= len(nums):
                return 0

            # Check the memo for any precalculated get_max_rob() at house i.
            # Simply return the value in the memo if we already calculated
            # before.
            if i in memo.keys():
                rob_this = memo[i]

            # Otherwise, calculate max rob if we decided to rob house i =
            # nums[i] + get_max_rob() at house i+2. Memoize the calculated
            # max rob at house i.
            else:
                rob_this = nums[i] + get_max_rob(nums, i + 2, memo)
                memo[i] = rob_this

            # If we decided to rob the next house over, i+1, instead of
            # house i, we need check if this house exist.
            rob_next = 0
            if i + 1 < len(nums):

                # Then, similar to rob_this, we check the memo for any
                # precalculated max rob values. Return the value in the memo
                # that is mapped to house i+1 if it exists as a key.
                if i + 1 in memo.keys():
                    rob_next = memo[i + 1]

                # Otherwise, calculate max rob if we decided to rob house i+1
                # = nums[i+1] + get_max_rob() at house i+3. Memoize the
                # calculated max rob at house i+1.
                else:
                    rob_next = nums[i + 1] + get_max_rob(nums, i + 3, memo)
                    memo[i + 1] = rob_next

            # Return whichever house that gives us a bigger rob: rob_this
            # house vs. rob_next house.
            return max(rob_this, rob_next)

        # This problem is different from the previous problem: House_Robber in
        # that the houses in this problem are arranged in a circle. Because of
        # this reason there is a chance that the previous algorithm might choose
        # to rob the first and the last house. This will be incorrect. Therefore,
        # we will solve this problem by starting from 3 different points:
        # 1) If we choose to rob the first house, then we might choose to rob
        #    the third house, but we cannot rob the last house.
        # 2) If we choose to rob the second house, then we can rob the last house.
        # 3) If we choose to rob the third house, then we can also rob the last
        #    house.
        # Then return the max of rob_first, rob_second, and rob_third.

        # If we choose to rob the first house, we cannot rob the last house.
        # Therefore we set the max rob memo at the last house to 0 in this case.
        memo = {
            len(nums)-1: 0
        }
        rob_first = nums[0] + get_max_rob(nums, 2, memo)

        # For starting house 2 or 3, we don't have the last house limitation.
        # Therefore, we clear the memo AS ALL THE CALCULATIONS ARE BASED ON THAT
        # LIMITATION IN ROBBING THE FIRST HOUSE. We will have to recalculate memo
        # without the last house calculation.
        rob_second = 0
        memo.clear()
        if 1 < len(nums):
            rob_second = nums[1] + get_max_rob(nums, 3, memo)

        # Calculate rob max if we decided to rob this first. NOTICE THAT, THE
        # CALCULATED MEMO AFTER ROB_FIRST MIGHT HAVE MEMO[3] MAX ROB VALUE.
        # HOWEVER, THIS VALUE WAS STILL BASED ON THE FACT THAT WE CANNOT ROB THE
        # LAST HOUSE. THEREFORE IT MAY NOT BE CORRECT IF WE DON'T HAVE THE LAST
        # HOUSE LIMITATION. We will have to recalculate rob_third. The good thing
        # is that we can reuse the calculated memo after rob_second as it doesn't
        # have the last house limitation.
        rob_third = 0
        if 2 < len(nums):
            rob_third = nums[2] + get_max_rob(nums, 4, memo)

        return max(rob_first, rob_second, rob_third)


n = [2,3,2]
sol = Solution().rob(n)
print(sol)
n = [1,2,3,1]
sol = Solution().rob(n)
print(sol)
n = [1,2,3]
sol = Solution().rob(n)
print(sol)
n = [2,1,1,2]
sol = Solution().rob(n)
print(sol)
n = [1,4,7,2,3]
sol = Solution().rob(n)
print(sol)
n = [1,9,7,2,10,3]
sol = Solution().rob(n)
print(sol)
n = [6,6,4,8,4,3,3,10]
sol = Solution().rob(n)
print(sol)
