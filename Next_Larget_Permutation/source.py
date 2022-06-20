class Solution:
    def nextPermutation(self, nums) -> None:

        # Strategy:
        # This is a pattern recognition problem.
        # Notice that, except for the corner case, the permutation that results
        # in the next larger number/permutation follows this pattern:
        # 1) Except for the corner case, there is a LAST OCCURRING index such that a[k] < a[k+1].
        # 2) For the next larger number/permutation, a[k] is swapped with the next larger number
        # somewhere in the tail starting from index k+1 to the end. Notice that the tail is.
        # inversely sorted. Otherwise, k and k+1 is not the LAST OCCURRING index such tha a[k] < a[k+1].
        # 3) Finally, we sort the tail from low to high. However, since we know that the tail is already
        # inversely sorted, we just have to flip it around.

        # Find the first decreasing pair from the right side.
        decreasing_idx = self.get_decreasing_index(nums)

        # Handling the corner case: the current permutation is already at maximum. There can be no
        # permutation that will be greater than the current permutation.
        if decreasing_idx == -1:
            nums.reverse()

        else:
            # Looking for the number at swap_idx to swap. The number that will swap with the position
            # at decreasing_idx needs to be the smallest number bigger than the number at decreasing_idx.
            swap_idx = decreasing_idx + 1
            while nums[decreasing_idx] < nums[swap_idx]:
                swap_idx += 1
                if swap_idx == len(nums):
                    break

            # At this point, we have found swap_idx. Swap the number at position decreasing_idx with
            # the number at swap_idx
            temp = nums[swap_idx-1]
            nums[swap_idx-1] = nums[decreasing_idx]
            nums[decreasing_idx] = temp

            # Finally, we sort the tail from high to low (which is the same as reversing the tail).
            self.flip_tail(nums, decreasing_idx+1)

        return None

    # Find the first decreasing pair from the right side.
    def get_decreasing_index(self, nums):

        for i in reversed(range(1, len(nums))):
            if nums[i] > nums[i-1]:
                return i-1

        return -1

    # Flip the tail around.
    def flip_tail(self, nums, start_idx):

        left = start_idx
        right = len(nums)-1
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

            left += 1
            right -= 1

        return None

number = [1,5,8,4,7,6,5,1]
Solution().nextPermutation(number)
print(number)
