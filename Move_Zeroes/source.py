class Solution:

    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Strategy:
        # We go through the list to find the 1st occurrence of zero and nonzero
        # until either of them are out of bound. We swap the position of the zero
        # and the nonzero element.
        # NOTE, we only swap the positions if zero element position is to the left of
        # the nonzero position

        # Find the very first occurrence of zero and nonzero
        zi = self.get_first_occurrence(nums, 0, len(nums), lambda x: x == 0)
        nzi = self.get_first_occurrence(nums, 0, len(nums), lambda x: x != 0)

        # Keep processing until the loop breaks. The loop breaks
        # when either the index of 1st occurrence of zero or the index of
        # 1st occurrence of nonzero is out of bound (cannot find it)
        while zi < len(nums) and nzi < len(nums):

            # If zi is to the left os nzi,
            # Swap the 1st occurrence position of the zero and nonzero element and
            # find both the next zi and the next nzi
            if zi < nzi:
                nums[zi], nums[nzi] = nums[nzi], nums[zi]
                zi = self.get_first_occurrence(nums, zi + 1, len(nums), lambda x: x == 0)

            # Otherwise, we keep the zi position and only find the next nzi
            nzi = self.get_first_occurrence(nums, nzi + 1, len(nums), lambda x: x != 0)

        return

    def get_first_occurrence(self, nums, start_index, end, break_condition):

        # While start_index is still within bound,
        # check to see if the break_condition (passed as a function pointer) is met
        while start_index < end:
            if break_condition(nums[start_index]):
                break
            start_index += 1

        return start_index


lst = [1,3,12,0,0]

Solution().moveZeroes(lst)

print(lst)
