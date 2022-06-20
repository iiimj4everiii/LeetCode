class Solution:
    def fourSum(self, nums, target: int):

        """"
        
        Algorithm

        We can implement k - 2 loops using a recursion. We will pass the starting point and k as the parameters.
        When k == 2, we will call twoSum, terminating the recursion.

        For the main function:
            Sort the input array nums.
            Call kSum function with start = 0, k = 4, and target, and return the result.

        For kSum function:
            Check if the sum of k smallest values is greater than target, or the sum of k largest values is smaller
            than target. Since the array is sorted, the smallest value is nums[start], and largest
            - the last element in nums.
                If so, no need to continue - there are no k elements that sum to target.

            If k equals 2, call twoSum and return the result.
            Iterate i through the array from start:
                If the current value is the same as the one before, skip it.
                Recursively call kSum with start = i + 1, k = k - 1, and target - nums[i].
                For each returned set of values:
                    Include the current value nums[i] into set.
                    Add set to the result res.
        Return the result res.

        For twoSum function:
            Set the low pointer lo to start, and high pointer hi to the last index.
            While low pointer is smaller than high:
                If the sum of nums[lo] and nums[hi] is less than target, increment lo.
                    Also increment lo if the value is the same as for lo - 1.
                If the sum is greater than target, decrement hi.
                    Also decrement hi if the value is the same as for hi + 1.
                Otherwise, we found a pair:
                    Add it to the result res.
                    Decrement hi and increment lo.
            Return the result res.

        """

        def kSum(nums, target: int, k: int):

            res = []

            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)

            return res

        def twoSum(nums, target: int):
            res = []
            lo, hi = 0, len(nums) - 1

            while lo < hi:
                sum = nums[lo] + nums[hi]

                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1

                elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1

                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

            return res

        nums.sort()

        return kSum(nums, target, 4)


n = [1,0,-1,0,-2,2]
print(Solution().fourSum(n, 0))
