class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:

        # Strategy:
        # This problem can be re-interpreted as finding duplicate within a window of size k + 1
        # Keep a set of visited integers in a window of size k
        # Iterate through nums list and see if nums[i] is in the window set
        # If it is, then we found a duplicate within the window
        # We will enforce size <= k window set at any time by removing oldest element in the set

        window = set()
        for i in range(len(nums)):

            # If we found an element in the size k window set, we found a duplicate
            if nums[i] in window:
                return True

            # Otherwise, add the new element to the window set
            window.add(nums[i])

            # If the window set becomes too large (> k),
            # remove the oldest element in the window set
            if len(window) > k:
                window.remove(nums[i-k])

        # At this point, there are no duplicates found
        return False

nums = [1,2,3,1,2,3]
print(Solution().containsNearbyDuplicate(nums, 2))
