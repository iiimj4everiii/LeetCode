class Solution:
    def summaryRanges(self, nums):

        # Create a return list that summarizes the ranges in str format
        summary_list = []

        # Handling corner cases
        if len(nums) == 0:
            return summary_list

        # Initialize start and current to nums[0]
        # start will hold the lower end of a range
        # current will traverse down the nums list, lagging behind nums[i] by 1 position
        # to see if there's a break in pattern (unit incrementation)
        start = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):

            # If there is a break in pattern (when num[i] > current+1),
            # generate a summary range string based on start and current
            if nums[i] > current+1:
                range_str = self.range_string(start, current)

                # Append the generated range string to our return summary_list
                summary_list.append(range_str)

                # Change the range start to nums[i]. This begins our next range pattern search
                start = nums[i]

            # Current keeps traversing down the nums list
            current = nums[i]

        # Handling the end corner cases because a break pattern at the end is not realized in the for loop
        # So we need to handle one last time outside of the loop.
        range_str = self.range_string(start, current)
        summary_list.append(range_str)

        return summary_list

    # If start == stop, then return "start"
    # Otherwise, return "start -> stop"
    def range_string(self, start, stop):
        if start == stop:
            return str(start)
        else:
            return str(start) + "->" + str(stop)


nums = [0,2,3,4,6,8,9]
print(Solution().summaryRanges(nums))
