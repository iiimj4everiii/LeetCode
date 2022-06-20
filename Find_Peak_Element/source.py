class Solution:
    def findPeakElement(self, nums) -> int:

        # Strategy:
        # If there a peak exists in a list of numbers,
        # there is a period of uptrend and a period of
        # downtrend. Since there is at least 1 peak in
        # this problem, there is at least 1 period of
        # uptrend and 1 period of downtrend. If we take
        # derivative of this list, we will have a zero-
        # crossing point at the peak. So we can do a
        # binary search of instantaneous derivative on
        # this list. If the slope if positive, we search
        # the right side of the list. Otherwise, we search
        # the left side of the list.

        # Initialize left to index 0 and right to index
        # len(nums) - 1
        left = 0
        right = len(nums)-1

        # While left index is still smaller than right
        # index.
        while left < right:

            # Get midpoint index between left and right.
            mid = (left + right) // 2

            # If the slope is positive, then the peak is
            # somewhere to the right of and including mid+1.
            # Bring left to mid + 1.
            if nums[mid+1] > nums[mid]:
                left = mid + 1

            # If the slope is negative, then the peak is
            # somewhere to the left of the including mid.
            # Bring right to mid.
            else:
                right = mid

        return left


n = [1,0]
sol = Solution().findPeakElement(n)
print(sol)
