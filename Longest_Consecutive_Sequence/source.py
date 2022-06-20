class Solution:
    def longestConsecutive(self, nums) -> int:

        # Strategy:
        # 1) We turn nums list to a set. This way, we can leverage O(1)
        #    lookup.
        # 2) Randomly select a number from nums_set.
        # 3) Then count the number of items to the left of it.
        # 4) Count the number of items to the right of it.
        # 5) Compare to the current longest consecutive count. Update it
        #    if the current count = left count + right count + 1 is greater
        #    than the current longest consecutive count.
        # 6) Every time we do an item/offsetted item lookup in nums_set, we
        #    remove from the set because we won't need it anymore. Only 1 and
        #    only 1 list will this item. If we don't remove it from
        #    nums_set, we might randomly select it again, ending up with the
        #    same list that contains this item.

        # A method to count the number items that are consecutively to the
        # left/right of item in nums_set.
        def get_consecutive(nums_set, item, get_item):

            # Starting with offset = 0,
            offset = 0
            while True:

                # If the item offsetted by offset is in nums_set, remove it
                # from nums_set and increment offset by 1.
                if get_item(item, offset) in nums_set:
                    nums_set.remove(get_item(item, offset))
                    offset += 1

                # Otherwise, break out of the loop and return.
                else:
                    break

            return offset

        # Turn nums list into a set. This should take O(n) time.
        nums_set = set(nums)

        # Initialize longest_consecutive to 0.
        longest_consecutive = 0

        # We keep processing until nums_set is empty.
        while len(nums_set) > 0:

            # Pop a random item from nums_set.
            rand_item = nums_set.pop()

            # Count all the items that are consecutively lower than rand_item.
            left_count = get_consecutive(nums_set, rand_item-1, lambda x, y: x-y)

            # Count all the items that are consecutively greater than rand_item.
            right_count = get_consecutive(nums_set, rand_item+1, lambda x, y: x+y)

            # Update longest_consecutive if the current consecutive count is greater
            # than the current longest_consecutive.
            longest_consecutive = max(longest_consecutive, left_count+right_count+1)

        return longest_consecutive


l = [0,3,7,2,5,8,4,6,0,1]
sol = Solution().longestConsecutive(l)
print(sol)
