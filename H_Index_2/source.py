class Solution:
    def hIndex(self, citations: list) -> int:

        # Strategy:
        # We will do binary search on citations. The the paper count
        # at index mid = len(citations) - mid. If the paper count is
        # greater than the citation[mid], then we move to the right
        # to look for bigger citation number. Otherwise, we move left
        # since we know that the h-index is at least =
        # len(citations) - mid. We will move left to look for a bigger
        # h-index.

        # Corner case: If no one cited any of the papers. Return 0.
        if citations[-1] == 0:
            return 0

        # Initialize left index to 0 and right index = len(citations)-1.
        left = 0
        right = len(citations)-1

        # We keep searching for the transitional point (first point that
        # satisfies the else statement) as long as the left index is
        # strictly less than the right index.
        while left < right:

            # Get the midpoint between left and right.
            mid = (left + right) // 2

            # The number of paper whose citation count is at least as
            # many as citation[mid].
            paper_count = len(citations) - mid

            # Now we test for qualifying h-index candidate.

            # If the number of paper, whose citation count is at least as
            # many as citation[mid], is greater than the least citation
            # count in the group = citation[mid], then we are too aggressive.
            # We need to search right.
            if paper_count > citations[mid]:
                left = mid + 1

            # Otherwise, we may not be aggressive enough, search left for
            # a possibly higher h-index value.
            else:
                right = mid

        return len(citations) - left


nums = [0, 0, 0, 2]
sol = Solution().hIndex(nums)
print(sol)
