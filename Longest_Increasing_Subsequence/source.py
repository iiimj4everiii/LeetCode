class Solution:
    def lengthOfLIS(self, nums: list) -> int:

        # Initialize LIS to a list of 1's as the LEAST increasing
        # subsequence is 1.
        LIS = [1 for _ in range(len(nums))]

        # Dynamic programming:
        # 1) Start with the second to last number nums[i] and compare
        #    it to all the numbers nums[j] to the right of it.
        #    a) If nums[i] < nums[j], update LIS[i] by taking the max
        #       of LIS[i] and 1 + LIS[j].
        # 2) Decrement index i by 1 until it reaches index 0.
        for i in range(len(nums)-2, -1, -1):
            for j in range(len(nums)-1, i, -1):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


main_nums = [10,9,2,5,3,7,101,18]
sol = Solution().lengthOfLIS(main_nums)
print(sol)
