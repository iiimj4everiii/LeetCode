class Solution:
    def removeElement(self, nums, val: int) -> int:
        for i in reversed(range(len(nums))):
            if nums[i] == val:
                nums.pop(i)

        return len(nums)


l = [0,1,2,2,3,0,4,2]
print(Solution().removeElement(l, 2))
print(l)