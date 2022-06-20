class Solution:
    def searchRange(self, nums, target: int):

        # Strategy:
        # Use 2 different version of binary search:
        # 1) Search for the first occurrence of target.
        # 2) Search for the last occurrence of target.
        # Then just return first and last occurrence in a list format.

        # Handling the corner case where nums is an empty list.
        if len(nums) == 0:
            return [-1, -1]

        # Finding the first occurring target in nums.
        first_occurring = self.binary_search_first_occurring(nums, target, 0, len(nums)-1)

        # At this point, we know if target exists in nums. If not, return [-1, -1].
        if nums[first_occurring] != target:
            return [-1, -1]

        # Finding the last occurring target in nums.
        last_occurring = self.binary_search_last_occurring(nums, target, 0, len(nums)-1)

        # Return the first and last occurrence in a list format.
        return [first_occurring, last_occurring]

    def binary_search_first_occurring(self, nums, target, left, right):

        while left < right:

            # We are calculating the floor of the midpoint between left and right.
            mid = (left + right) // 2

            if nums[mid] < target:

                # Notice that we advance left to mid+1 instead of mid.
                # This is because:
                # 1) mid is the floor(average of left and right). So mid can get stuck at the same point.
                # 2) since the condition is strictly for LESS THAN target, we know that nums[mid] cannot
                # be the target. So we advance to mid+1 instead.
                left = mid + 1

            else:

                # At this point, nums[mid] is greater than OR EQUAL TO target. So we need to keep mid.
                right = mid

        return left

    def binary_search_last_occurring(self, nums, target, left, right):

        while left < right:

            # We are calculating the ceiling of the midpoint instead of the floor of the midpoint.
            mid = (left + right + 1) // 2

            if nums[mid] <= target:

                # Notice that we advance left to mid instead of mid+1 in the previous case.
                # This is because at this point, nums[mid] is less than OR EQUAL TO target.
                # So we need to keep mid.
                left = mid

            else:

                # Notice that we advance left to mid-1 instead of mid.
                # This is because:
                # 1) mid is the ceiling(average of left and right) instead of the floor(average of left
                # and right). We accomplish this by calculating (left + right + 1) // 2 instead of
                # (left + right) // 2.
                # 2) since the condition is strictly for GREATER THAN target, we know that nums[mid] cannot
                # be the target. So we advance to mid-1 instead.
                right = mid - 1

        return left


# n = [5,7,7,8,8,10]
# n = []
n = [5,7,7,10]
print(Solution().searchRange(n, 8))
