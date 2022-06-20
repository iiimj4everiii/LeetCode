# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n) -> int:
        """
        :type n: int
        :rtype: int
        """

        # You are a product manager and currently leading a team to develop a new product.
        # Unfortunately, the latest version of your product fails the quality check.
        # Since each version is developed based on the previous version,
        # all the versions after a bad version are also bad.

        # Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
        # which causes all the following ones to be bad.

        # You are given an API bool isBadVersion(version) which returns whether version is bad.
        # Implement a function to find the first bad version. You should minimize the number of calls to the API.

        # Strategy:
        # This is a binary search problem and can be done in O(logn) time
        # We start from the middle. If that's a bad version,we search left and including mid
        # Otherwise, we search the right of mid. We keep doing this until i == j or j = i + 1
        # The loop invariance of this binary search is that i always a good version
        # and j is always a bad version except for a corner case: the 0th version is already bad

        # Handing corner cases:
        if isBadVersion(0):
            return 0

        # Initialize i to be the left most index and n to be the right most index of the versions array
        i = 0
        j = n

        # We keep doing binary search until we arrive at the end of the search point (either i == j or j = i + 1)
        while j - i > 1:

            # Find the midpoint between i and j
            mid = (i + j) // 2

            # If the mid version is bad, then we know the first bad version is to the left and including mid.
            if isBadVersion(mid):
                j = mid

            # Otherwise, we know the last good version is to the right and including mid
            else:
                i = mid

        # At this point, we either have:
        # i == j, in this case i/j is the first bad version
        # j > i, in this case j is the first bad version
        # So in both cases, j is the first bad version

        return j



print(Solution().firstBadVersion())
