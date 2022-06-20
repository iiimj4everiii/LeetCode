class Solution:
    def twoSum(self, nums, target):
        nums_dict = dict()
        for i in range(len(nums)):
            key = nums[i]
            value = i
            if key not in nums_dict.keys():
                nums_dict[key] = []
            nums_dict[key].append(value)

        for first_num in nums:
            second_num = target - first_num

            first_val = nums_dict[first_num].pop()

            if second_num not in nums_dict.keys():
                continue

            if len(nums_dict[second_num]) > 0:
                second_val = nums_dict[second_num].pop()

                return sorted([first_val, second_val])

        return [-1, -1]

    # Only works for list of unique integers
    def twoSum2(self, nums, target):
        target_minus_nums = [target - n for n in nums]

        intersect = set(nums).intersection(target_minus_nums)

        indices = [nums.index(i) for i in intersect]

        return sorted(indices)

    # Using the property of this problem
    def twoSum3(self, nums, target):

        # Sort the list in ascending order
        sorted_nums = sorted(nums)

        # The corresponding indices of the sorted list
        sorted_index = sorted(range(len(nums)), key=nums.__getitem__)

        i = 0
        j = len(nums) - 1
        while i < j:

            # The sum of the current leftmost (lowest) number and the current rightmost (highest) number
            s = sorted_nums[i] + sorted_nums[j]

            # If the s is the target, then we are done
            if s == target:
                index1 = sorted_index[i]
                index2 = sorted_index[j]
                return sorted([index1, index2])

            # If s < target, then we move the left index to the right
            elif s < target:
                i += 1

            # If s > target, then we move the right index to the left
            else:
                j -= 1

        return [-1, -1]


l = [3, 2, 4, 13]
solution = Solution().twoSum(l, 6)
print(solution)

solution2 = Solution().twoSum2(l, 6)
print(solution2)

solution3 = Solution().twoSum3(l, 6)
print(solution3)
