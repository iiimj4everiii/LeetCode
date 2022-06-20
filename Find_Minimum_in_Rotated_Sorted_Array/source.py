class Solution:
    def findMin(self, nums) -> int:

        # Strategy:
        # If nums is sorted already, just return the leftmost number.
        # An increasingly sorted array of unique numbers will always
        # have the leftmost number less than the rightmost number. If
        # this is the case, just return the leftmost number. If nums,
        # is rotated, then the leftmost number will always be greater
        # than the rightmost number.

        # We examine the middle number.
        # If the middle number is less than the leftmost number, then
        # our minimum exists somewhere between the left index and the
        # midpoint index. We bring the right index to the midpoint.
        # Otherwise, minimum exists somewhere between midpoint+1 and
        # the right index. We bring left index to the midpoint.

        # Initialize l index and r index to 0 and -1 respectively.
        l = 0
        r = len(nums) - 1

        # Corner case: if nums is already in the correct sorted order,
        # just return the left number.
        left = nums[0]
        if left < nums[r]:
            return left

        # At this point, we know that nums is rotated.
        while l < r:

            # Find the midpoint between l and r.
            m = (l + r) // 2

            if nums[m] < left:
                # m is in the rotated side. The lowest number
                # should be either at m or to the left of m. No
                # need to explore the right side, so bring r to m.
                r = m

            else:
                # m is in the original side. The lowest number can
                # be in either side depending on if
                l = m + 1

        return nums[l]


n = [8,1,2,3,4,5,6,7]
sol = Solution().findMin(n)
print(sol)
