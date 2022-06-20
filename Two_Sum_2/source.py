class Solution:
    # def twoSum(self, numbers, target):
    #
    #     # The tricky part is that these 2 numbers can be the same and
    #     # they may or may not be 2 of these numbers in the numbers list
    #
    #     # For each element in numbers
    #     for n in numbers:
    #
    #         # Calculate the diff and see if diff is also in the numbers list
    #         diff = target - n
    #
    #         # If n == diff, then we need to check if we have 2 elements of n
    #         # next to each other.
    #         if n == diff:
    #             m = numbers[numbers.index(n)+1]
    #             if m == diff:
    #                 return [numbers.index(n)+1, numbers.index(n)+2]
    #
    #         # Return the index of n and diff if they both exist in numbers list
    #         if diff in numbers:
    #             return [numbers.index(n)+1, numbers.index(diff)+1]

    def twoSum(self, numbers, target):

        # The tricky part is that these 2 numbers can be the same and
        # they may or may not be 2 of these numbers in the numbers list

        # Strategy: since we know the solution exist, we can search for it
        # by moving the indices towards each other starting from the far end
        # of the numbers list.
        # On the left side, we start from the first element and move towards the right.
        # On the right side, we start from the last element and move towards the left.
        # If the sum of those are greater than the target, we move the right index to the left.
        # If the sum of those are less than the target, we move the left index to the right.

        # Initialize the left and right index
        left_index = 0
        right_index = len(numbers)-1

        while True:

            # Get the number at index left_index and right_index
            left_number = numbers[left_index]
            right_number = numbers[right_index]

            # Get their sum
            two_sum = left_number + right_number

            # If the sum is less than target, then we know the left_number is too small
            if target > two_sum:
                left_index += 1

            # If the sum is greater than target, then we know the right_number is too large
            elif target < two_sum:
                right_index -= 1

            # Otherwise, we found the two_sum
            else:
                return [left_index+1, right_index+1]


l = [2,7,11,15]
print(Solution().twoSum(l, 18))
