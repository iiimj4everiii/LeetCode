class Solution:
    def majorityElement(self, nums: list) -> list:

        # Strategy:
        # We will use a modified version of Boyer-Moore's
        # Voting algorithm to keep track of 2 majorities.
        candidate1, candidate2 = \
            self.two_candidates_boyer_moore_voting_algo(nums)

        # Initialize our return list to empty list.
        res = []

        # Count the number of candidate1 in nums
        count1 = nums.count(candidate1)

        # Count the number of candidate2 in nums
        count2 = nums.count(candidate2)

        # If count1 is more than 1/3 of number of elements,
        # append candidate1 to res list.
        if count1 > len(nums) // 3:
            res.append(candidate1)

        # Likewise, if count2 is more than 1/3 of number of
        # elements, append candidate2 to res list.
        if count2 > len(nums) // 3:
            res.append(candidate2)

        return res

    @staticmethod
    def two_candidates_boyer_moore_voting_algo(nums: list):

        # Initialize candidate1 and candidate2 to None. Also
        # initialize their leading vote count to 0.
        candidate1 = None
        candidate2 = None
        lead_count1 = 0
        lead_count2 = 0

        # Go through elements in nums:list
        for n in nums:

            # If the vote, n, is for one of the majority:
            # candidate1, then we increase candidate1's lead
            # (lead_count1) by 1.
            if n == candidate1:
                lead_count1 += 1

            # If the vote, n, is for the other majority:
            # candidate2, then we increase candidate2's lead
            # (lead_count2) by 1.
            elif n == candidate2:
                lead_count2 += 1

            # If candidate1 is no longer leading, we replace
            # candidate1 with our new candidate: n
            elif lead_count1 == 0:
                candidate1 = n
                lead_count1 = 1

            # If candidate2 is no longer leading, we replace
            # candidate2 with our new candidate: n
            elif lead_count2 == 0:
                candidate2 = n
                lead_count2 = 1

            # Otherwise, we decrease the leading count for both
            # candidate1 and candidate2 by 1 vote.
            else:
                lead_count1 -= 1
                lead_count2 -= 1

        # Return top 2 candidates.
        return candidate1, candidate2


nums = [4,1,1,1,3,2,4,2,2,1]
# nums = [2,2,1,3]
sol = Solution().majorityElement(nums)
print(sol)
