class Solution:
    def hIndex(self, citations: list) -> int:

        # Strategy:
        # We will break citation counts into 2 groups:
        # 1) All the papers whose citation count is at least as
        #    many as total number of published papers n.
        # 2) All the papers whose citation count is strictly less
        #    than the total number of published papers n.
        # Then we do a cumulative sum of paper count from the
        # highest h-index value to the lowest h-index value. When the
        # cumulative sum at index h_idx is at least as large as h_idx
        # itself, then this is our highest h-index value of our
        # researcher.

        # Get the number of published research paper.
        n = len(citations)

        # The extra space is for papers that receives 0 citations.
        paper_count = [0] * (n+1)

        # We will let the highest possible h-index value to represent
        # all the papers that has at least as many citation count as
        # n. The highest possible h-index we can get is n. Therefore,
        # all the papers that has at least as many citation count as
        # n will be stored in paper[n].
        for i in citations:
            if i >= n:
                paper_count[n] += 1
            else:
                paper_count[i] += 1

        # Initialize cumulative_sum to 0.
        cumulative_sum = 0
        for h_idx in range(n, -1, -1):

            # We calculate the cumulative sum (of paper count) starting
            # from the the paper count in the highest possible h-index,
            # n, to the lowest possible h-index, 0.
            cumulative_sum += paper_count[h_idx]

            # If at h_idx, the cumulative sum of paper count is at
            # least h_idx, then this h_idx is the highest h-index value
            # of the researcher. Return h_idx
            if cumulative_sum >= h_idx:
                return h_idx


nums = [3,0,6,1,5]
sol = Solution().hIndex(nums)
print(sol)
