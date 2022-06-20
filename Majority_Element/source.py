class Solution:
    # def majorityElement(self, nums) -> int:
    #
    #     # This is basically a median finding problem because majority element
    #     # (occurs more than half) is also going to be the median element
    #     # We can do this in linear time if we use median-of-medians finding algorithm
    #     # To simplify our solution, we just sort and return the middle element
    #
    #     # Sort the nums list
    #     nums.sort()
    #
    #     # Get the middle index
    #     mid = len(nums) // 2
    #
    #     # Return the middle index of the sorted nums list (the median)
    #     return nums[mid]

    def majorityElement(self, nums) -> int:

        # Using Boyer-Moore Voting Algorithm O(n) time complexity O(1) space complexity
        # The algorithm keeps the current majority and its count
        # Its count goes up if the subsequent element is the same, else its count goes down
        # When the count goes down to 0, we can forget all the elements we saw
        # up to that point.

        # INSIGHT: We can forget all the elements up to that point because we know there
        # will always be more majority than all the minorities combined!
        # All the minorities will essentially be cancelled out by the majority plus some
        # So at the end, the majority will stand out, even if it is by a hair

        majority = nums[0]
        majority_count = 1

        for n in nums[1:]:
            if majority_count == 0:
                majority = n

            if n == majority:
                majority_count += 1
            else:
                majority_count -= 1

        return majority

nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))
