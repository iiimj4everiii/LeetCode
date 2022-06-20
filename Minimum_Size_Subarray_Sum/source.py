class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:

        # Initialize left and right index to 0
        left = 0
        right = 0

        # Initialize length to an impossibly large number: larger
        # than the size of nums itself.
        length = len(nums) + 1

        # Since we know there is at least 1 element in nums,
        # initialize total to the first element.
        total = nums[0]
        while left <= right:

            # If total is less than target, we advance right index
            # 1 step to the right. Then add the number at the new
            # right index to total.
            if total < target:
                right += 1

                # If we are out of bound, break and return.
                if right == len(nums):
                    break

                total += nums[right]

            # Otherwise, we get the length of the sub-array and
            # update it if the new length is less than the previous
            # sub-array length. sub-array length = (right - left + 1)
            else:
                length = min(length, right - left + 1)

                # Subtract the number at the current left index from
                # total and advance left index 1 step to the right.
                total -= nums[left]
                left += 1

        # If length is still bigger than the size of nums list, then
        # we cannot find a contiguous sub-array that sums to or greater
        # than target. Return 0 in this case for not found.
        if length == len(nums) + 1:
            return 0

        return length



n = [2,3,1,2,4,3]
sol = Solution().minSubArrayLen(7, n)
print(sol)
n = [1,2,3,4,5]
sol = Solution().minSubArrayLen(11, n)
print(sol)
n = [1,4,4]
sol = Solution().minSubArrayLen(4, n)
print(sol)
n = [1,1,1,1,1,1,1,1]
sol = Solution().minSubArrayLen(11, n)
print(sol)
n = [2,16,14,15]
sol = Solution().minSubArrayLen(20, n)
print(sol)

