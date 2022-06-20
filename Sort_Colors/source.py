class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Problem:
        # Given an array nums with n objects colored red, white, or blue,
        # sort them in-place so that objects of the same color are adjacent,
        # with the colors in the order red, white, and blue.
        # We will use the integers 0, 1, and 2 to represent the color red,
        # white, and blue, respectively.
        # You must solve this problem without using the library's sort function.

        # Strategy:
        # Since there are only 3 different colors, we can use Counting sort.

        # Initialize the count number of each color to 0.
        color_counts = [0] * 3

        # Get the count number of each color by incrementing the current count
        # at their respective index.
        for n in nums:
            color_counts[n] += 1

        # Go through nums and redistribute the color until the count reaches 0.
        # If we do this from left to right on color_counts list, we will get
        # a sorted list (nums).
        idx = 0
        for color in range(3):

            # Get the count of color
            color_count = color_counts[color]

            # For color_count number of times, we distribute color to nums.
            # Then move onto the next index in nums.
            for _ in range(color_count):
                nums[idx] = color
                idx += 1

        return None


c = [1]
Solution().sortColors(c)
print(c)
