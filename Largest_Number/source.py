class LargerNumKey(str):
    def __lt__(self, other):
        return self+other > other+self

class Solution:
    def largestNumber(self, nums) -> str:

        nums_str = [""] * len(nums)
        for i in range(len(nums)):
            nums_str[i] = str(nums[i])

        nums_str_sorted = sorted(nums_str, key=LargerNumKey)

        res = ""
        for z in nums_str_sorted:
            res += z

        if res[0] == '0':
            return '0'

        return res


n = [0,0]
sol = Solution().largestNumber(n)
print(sol)

def f(student):
    return student[2]

def g(x, y):
    return x+y > y+x