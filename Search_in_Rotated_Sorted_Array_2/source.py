class Solution:
    def search(self, nums, target: int) -> int:

        # Strategy:
        # Since the numbers in nums may not be distinct, we need another algorithm
        # to see whether or not target exists in nums as fast as we can.
        # Similar to the previous algorithm for the problem:
        # Search_in_Rotated_Sorted_Array, we first find out whether target might be
        # in the un-rotated side of the array or the rotated side of the array.
        # Unless the first element of nums nums[0] is equal to target, in which case
        # we just return True, we have to find the rotation pivot. Once we find this
        # pivot, we do binary search between 0 and pivot if target might be in the
        # un-rotated side or between pivot and end if target might be in the rotated
        # side. If pivot is -1, that means target is either smaller than the smallest
        # number in nums or larger than the largest number in nums. Return False in
        # both cases.

        # Find the pivot:
        # On the un-rotated side, find the index in nums that contains number
        # greater than or equal to target.
        # On the rotated side, find the index in nums that contains number less
        # than or equal to target.
        def find_pivot(nums: list, target: int, left: int, right: int, cond) -> int:

            # If the left index and the right index lines up,
            if left == right:

                # check to see if nums at this index is equal to the target.
                if cond(nums[left], target):
                    # Return the index if so.
                    return left

                # Otherwise, return a not-found flag = -1.
                else:
                    return -1

            # If the left index and the right index does NOT line up, then we
            # recurse. Find the midpoint and see if that's a pivot.
            mid = (left + right) // 2
            if cond(nums[mid], target):
                return mid

            # If not, then recurse left to see if we can find the pivot.
            pivot = find_pivot(nums, target, left, mid, cond)
            if pivot >= 0:
                return pivot

            # If not, then recurse right to see if we can find the pivot.
            return find_pivot(nums, target, mid+1, right, cond)

        # A typical binary search algorithm.
        def binary_search(nums: list, target: int, left: int, right: int):

            while left < right:

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

        # if nums[0] == target, return True
        if nums[0] == target:
            return True

        # If nums[0] < target, search the un-rotated side
        elif nums[0] < target:

            # Find the pivot by looking for a number in nums that is greater than
            # or equal to the target.
            pivot = find_pivot(nums, target, 0, len(nums)-1, lambda x, y: x >= y)

            # If find_pivot cannot find a number in nums that is greater than or
            # equal to the target, that means target is bigger than the largest
            # number in nums. Return False since target cannot be found in nums.
            if pivot == -1:
                return False

            # Otherwise, use binary search to find the index that target can be
            # in the un-rotated side from index 0 to the pivot.
            idx = binary_search(nums, target, 0, pivot)

        # If nums[0] > target, search the rotated side
        else:
            # Find the pivot by looking for a number in nums that is less than
            # or equal to the target.
            pivot = find_pivot(nums, target, 0, len(nums)-1, lambda x, y: x <= y)

            # If find_pivot cannot find a number in nums that is less than or
            # equal to the target, that means target is smaller than the smallest
            # number in nums. Return False since target cannot be found in nums.
            if pivot == -1:
                return False

            # Otherwise, use binary search to find the index that target can be
            # in the rotated side from pivot to the end.
            idx = binary_search(nums, target, pivot, len(nums)-1)

        # Return True if nums[idx] is equal to target. False otherwise.
        return nums[idx] == target


n = [1,1,1,1,1,1,2]
print(Solution().search(n, 2))
