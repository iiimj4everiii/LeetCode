class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:

        # Strategy:
        # This is a selection problem. The O(n) solution is
        # complicated to implement and therefore we will solve it
        # using partitions instead. The numbers in this problem can
        # be repeated. Therefore to avoid the consequences of getting
        # the worst case scenario input num, we will randomly select
        # the pivot AND create 3 partitions instead of 2: left, right,
        # and mid. This will help us if the input nums contains many
        # of the same number.

        from random import randint

        def get_kth_largest(nums, k) -> int:

            # Corner case 1: If we are looking for the largest number,
            # simply return max of nums. O(n) time complexity.
            if k == 0:
                return max(nums)

            # Corner case 2: If we are looking for the smallest number,
            # simply return min of nums. O(n) time complexity.
            if k == len(nums):
                return min(nums)

            # We randomly select a number in nums as our pivot. It is
            # important to use random select as it reduces the chance
            # of worst case scenarios.

            # Get a random index in nums.
            random_idx = randint(0, len(nums)-1)

            # Our pivot will be nums[random_idx].
            pivot = nums[random_idx]

            # # Swap the number in the last index with pivot. This way,
            # # pivot will be at the end and we can go through nums from
            # # index 0 to but not including the end.
            # nums[random_idx] = nums[-1]
            # nums[-1] = pivot

            # Initialize left, mid, and right partitioned lists to empty
            # lists. Left will hold all the numbers strictly less than
            # the pivot. Mid will hold all the numbers equal to pivot.
            # Right will hold all the numbers strictly greater than pivot.
            # This should help in situation where the numbers in nums are
            # all the same number.
            left = []
            mid = []
            right = []
            for n in nums:
                if n == pivot:
                    mid.append(n)
                elif n < pivot:
                    left.append(n)
                else:
                    right.append(n)

            # Get the position of the right-most pivot.
            pivot_right = len(right) + 1

            # Get the position of the left-most pivot.
            pivot_left = len(right) + len(mid)

            # If position k is between left-most and right-most pivot,
            # then we found the kth largest number. It is in the mid
            # list and therefore the kth largest number is the pivot.
            if pivot_right <= k <= pivot_left:
                return pivot

            # If k is smaller than pivot_right, then the kth largest
            # number is still in the right list.
            if k < pivot_right:
                return self.findKthLargest(right, k)

            # Otherwise, the kth largest number is somewhere in the left
            # list.
            return self.findKthLargest(left, k - pivot_left)

        return get_kth_largest(nums, k)


n = [3,2,1,5,6,4]
sol = Solution().findKthLargest(n, 2)
print(sol)
