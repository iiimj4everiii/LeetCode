class Solution:
    def productExceptSelf(self, nums: list):

        # Strategy: O(n) runtime WITHOUT USING DIVISION
        # This is a dynamic programming problem. Notice:
        # if nums = [a,     b,      c,      d   ], then
        # the res = [bcd,   acd,    abd,    abc ]. If we
        # do cumulative product starting from the left,
        # we get    [a,     ab,     abc,    abcd]. Likewise
        # if we do cumulative product starting from the right,
        # we get    [abcd,  bcd,    cd,     d   ].
        # Therefore, res[k] = left[k-1] * right[k+1]

        # Cumulative product starting from the left hand side.
        # We pad the left list with 2 additional spaces: 1 at
        # the starting index and 1 at the ending index. These
        # 2 locations will be initialized with 1.
        left = [1] * (len(nums) + 2)
        for i in range(1, len(nums)+1):
            left[i] = left[i-1] * nums[i-1]

        # Cumulative product starting from the right hand side.
        # Likewise, we pad the right list with 2 additional
        # spaces: 1 at the starting index and 1 at the ending
        # index. These 2 locations will be initialized with 1.
        right = [1] * (len(nums) + 2)
        for i in reversed(range(1, len(nums)+1)):
            right[i] = right[i+1] * nums[i-1]

        # INSIGHT: res[k] = left[k - 1] * right[k + 1]
        res = [1] * (len(nums) + 2)
        for i in range(1, len(nums)+1):
            res[i] = left[i-1] * right[i+1]

        # Only return res list from index 1 to -1
        return res[1:-1]


sol = Solution().productExceptSelf([1,2,3,4])
print(sol)
