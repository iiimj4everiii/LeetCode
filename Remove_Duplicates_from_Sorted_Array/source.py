class Solution:
    def removeDuplicates(self, nums) -> int:

        if len(nums) > 0:

            prev_n = nums[0]
            for n in nums[1:]:
                if n == prev_n:
                    nums.remove(n)
                else:
                    prev_n = n

        return len(nums)

    # Much faster. pop() might be faster than remove()
    def removeDuplicates2(self, nums) -> int:

        if len(nums) > 0:

            prev_n = nums[-1]
            for i in range(len(nums[1:])-1, -1, -1):
                if nums[i] == prev_n:
                    nums.pop(i)
                else:
                    prev_n = nums[i]

        return len(nums)

nums = []

print(Solution().removeDuplicates2(nums))
print(nums)