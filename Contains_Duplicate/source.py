class Solution:
    def containsDuplicate(self, nums) -> bool:

        # Strategy:
        # Keep a set of all the visited integers
        # Iterate through the list
        # If we encounter an integer that we already seen (in the visited set)
        # Then we have found a duplicate
        # If we never come across such an event, then there are no duplicates

        visited = set()

        for n in nums:

            # If we encounter an integer that we already seen (in the visited set)
            # Then we have found a duplicate
            if n in visited:
                return True

            # Otherwise, we add n to our visited set
            visited.add(n)

        # At this point, we never came across an n that has been added to the visited set
        return False


nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))
