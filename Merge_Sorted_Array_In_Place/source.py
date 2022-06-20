class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0
        # Go through both lists from left to right
        # Insert elements from num2 into num1 (in place) if nums2[j] < nums1[i]
        # Stop when either index (i or j) is at the end
        while i < m and j < n:
            if nums2[j] < nums1[i]:
                self.shift_elements_down_by_one(nums1, i, m)
                nums1[i] = nums2[j]
                j += 1
                m += 1

            i += 1

        # At this point, we either have 2 sorted list with all the elements in nums2 > all the elements in nums1
        # or all the elements are in nums1 while nothing left in nums2
        # Either way, we copy whatever that is left in nums2 to the end of nums1
        nums1[m:] = nums2[j:]

        return

    def shift_elements_down_by_one(self, nums1, i_start, i_end):
        while i_end > i_start:
            temp = nums1[i_end]
            nums1[i_end] = nums1[i_end-1]
            nums1[i_end-1] = temp
            i_end -= 1


nums1 = []
nums2 = []
Solution().merge(nums1, len(nums1)-len(nums2), nums2, len(nums2))
print(nums1)
