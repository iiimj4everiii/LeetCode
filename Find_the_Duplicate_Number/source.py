class Solution:

    # # Negative marking solution: Since all the numbers in nums are
    # # positive, we can mark these numbers negative as a flag to
    # # indicate seen.
    # def findDuplicate(self, nums) -> int:
    #
    #     # Strategy:
    #     # Instead of exploring the nums list sequentially from left
    #     # to right or from right to left, we will explore the list
    #     # like a linked list. THIS IS ONLY POSSIBLE BECAUSE ALL THE
    #     # NUMBERS IN NUMS ARE WITHIN THE RANGE OF THE LIST INDICES.
    #
    #     # Initialize the exploration index to 0.
    #     idx = 0
    #
    #     # Keep exploring until we find a negatively marked number.
    #     while True:
    #
    #         # Get the next index. THE NEXT INDEX IS THE VALUE HELD
    #         # IN THE CURRENT INDEXED POSITION. THIS IS SIMILAR TO
    #         # TRAVERSING A LINKED LIST.
    #         next_idx = nums[idx]
    #
    #         # If the number/next_idx is negatively marked, we found
    #         # the duplicate number: idx. Break out of the loop.
    #         if next_idx < 0:
    #             break
    #
    #         # Otherwise, mark the number negative and update the
    #         # exploration idx to next_idx.
    #         nums[idx] *= -1
    #         idx = next_idx
    #
    #     # In this problem, we are not allowed to change nums:list,
    #     # so we get rid of all the negative markings in nums before
    #     # returning the duplicate number.
    #     for i in range(len(nums)):
    #         nums[i] = abs(nums[i])
    #
    #     return idx

    # Turtle and Hare cycle detection method: We treat the numbers in
    # nums as "nodes" in a linked list and the numbers themselves are
    # "pointers" to the next "node". Since there is at most 1 repeated
    # number in nums, we can look at the list as a linked list with 1
    # "node", the repeated "node", pointed by more than 1 other "nodes".
    def findDuplicate(self, nums) -> int:

        # Strategy:
        # After translating this problem to a cycle detection problem,
        # we just need to find out the first node where the cycle began.
        # We did this before:
        # 1) Find the node where turtle/slow and the hare/fast meets up.
        # 2) Take turtle/slow back to the starting point and slow the
        #    hare/fast down. Move them until they meet up again. The
        #    node where they meet up for the second time is the entrance
        #    into the cycle.

        # Initialize turtle and hare's starting position.
        turtle = 0
        hare = 0

        # 1) Find the node where turtle/slow and the hare/fast meets up.
        while True:
            turtle = nums[turtle]

            hare = nums[hare]
            hare = nums[hare]

            if turtle == hare:
                break

        # 2) Take turtle/slow back to the starting point.
        turtle = 0

        # slow the hare/fast down. Move them until they meet up again.
        # The node where they meet up for the second time is the
        # entrance into the cycle - translating to the duplicate number.
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[hare]

        return turtle


main_nums = [3,1,3,2,4]
sol = Solution().findDuplicate(main_nums)
print(sol)
