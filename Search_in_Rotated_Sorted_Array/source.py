class Solution:
    def search(self, nums, target: int) -> int:

        # Strategy:
        # We are using binary search approach to reduce search time to O(log n) time.
        # However, since nums is rotated, we need to find out which side the target
        # might be in. To find out which side target might be in, we do a quick test
        # against the first element of nums. Since nums is sorted in ascending order,
        # except for that rotated point, we can leverage this information. If nums[0]
        # is smaller than target, that means target might be somewhere left of the pivot
        # point. Otherwise, target might be somewhere to the right of the pivot point.

        left = 0
        right = len(nums)-1

        # Handling corner case 1: target is in the 0th index.
        if nums[0] == target:
            return 0

        # Handling corner case 2: target is in the last index.
        if nums[-1] == target:
            return len(nums)-1

        if nums[0] < target:

            # Search the un-rotated side
            right = max(right - 1, 0)
            while left < right:

                # Calculate the midpoint = floor(average(left, right))
                mid = (left + right) // 2

                # We are looking for the pivot REGION. We can ignore everything to the right
                # of where the target location is. That is all the numbers greater than target
                # and everything to the right of it.
                if nums[mid] >= target:

                    # Once we find a pivot point, we move the right index to this point.
                    right = mid
                    break

                # We have 2 cases where nums[mid] is LESS THAN target:
                # 1) nums[mid] is on the un-rotated side and to the left of target
                # 2) nums[mid] is on the rotated side and to the right of target
                else:

                    # We test if nums[mid] < nums[0]. If it is true, then mid is currently on the
                    # rotated side. We move the right index to mid-1 (since we know mid is
                    # not the correct index).
                    if nums[mid] < nums[0]:
                        right = mid - 1

                    # Otherwise, we know mid is currently on the un-rotated side. We move the
                    # left index to mid+1 (since we know mid is not the correct index).
                    else:
                        left = mid + 1

        else:
            # Search the rotated side
            left = min(left + 1, len(nums)-1)
            while left < right:

                # Calculate the midpoint = floor(average(left, right))
                mid = (left + right) // 2

                # We are looking for the pivot REGION. We can ignore everything to the left
                # of where the target location is. That is all the numbers less than target
                # and everything to the left of it.
                if nums[mid] <= target:

                    # Once we find a pivot point, we move the left index to this point.
                    left = mid
                    break

                # We have 2 cases where nums[mid] is GREATER THAN target:
                # 1) nums[mid] is on the un-rotated side and to the left of target
                # 2) nums[mid] is on the rotated side and to the right of target
                else:

                    # We test if nums[mid] > nums[0]. If it is true, then mid is currently on the
                    # un-rotated side. We move the left index to mid+1 (since we know mid is
                    # not the correct index).
                    if nums[mid] > nums[0]:
                        left = mid + 1

                    # Otherwise, we know mid is currently on the rotated side. We move the
                    # right index to mid-1 (since we know mid is not the correct index).
                    else:
                        right = mid - 1

        # Get the index where target should be.
        index = self.normal_binary_search(nums, target, left, right)

        # Check if nums[index] is the target number.
        if nums[index] == target:
            return index
        else:
            return -1

    def normal_binary_search(self, nums, target, left, right):

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


n = [5,1,2,3,4]
# n = [3, 1]
# n = [4,5,6,7,0,1,2]
# n = [1]
# n = [1, 3]
print(Solution().search(n, 1))