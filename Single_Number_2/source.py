class Solution:
    def singleNumber(self, nums) -> int:

        # Problem:
        # Given an integer array nums where every element appears
        # three times except for one, which appears exactly once.
        # Find the single element and return it.
        # You must implement a solution with a linear runtime
        # complexity and use only constant extra space.

        # Strategy:
        # The solution to this problem is very strange as there
        # is no direct way to tackle this problem. The idea is to
        # encode all the numbers in nums and count them in the
        # encoded form. In our solution, we use binary encoding
        # of each number and count the 1's bit in all 32 positions.
        # After summing up the positional bit counts for all the
        # numbers in nums, we take the mod 3 of 32 positional bit
        # counts. Whatever that is left over is the binary encoded
        # number that is not a triplet.

        # Function that converts an integer to a binary number
        # spread out across 33-sized array of integers. The extra
        # bit is for the polarity.
        def int2bin_array(num):
            binary = bin(num)
            binary_len = len(binary)

            bin_array = [0] * 33

            negative_offset = 0
            if binary[0] == '-':
                negative_offset = 1
                bin_array[-1] = 1

            for i in range(2+negative_offset, binary_len):
                bin_array[binary_len-1-i] = int(binary[i])

            return bin_array

        # Adding list l2 to l1.
        def list_sum(l1, l2):
            for i in range(len(l1)):
                l1[i] += l2[i]

            return

        # Initialize size 33 count array/list to 0's
        counter = [0] * 33

        # Go through nums, then convert each number to binary
        # array and add to counter.
        for n in nums:
            list_sum(counter, int2bin_array(n))

        # Take mod 3 for each positional bit count.
        for i in range(33):
            counter[i] = counter[i] % 3

        # Convert the leftover in binary form to decimal
        total = 0
        for i in range(32):
            total += counter[i] * 2 ** i

        if counter[-1] == 1:
            total = -total

        # Return the decimal form of the leftover.
        return total


nums = [-401451,-177656,-2147483646,-473874,-814645,-2147483646,-852036,-457533,-401451,-473874,-401451,-216555,-917279,-457533,-852036,-457533,-177656,-2147483646,-177656,-917279,-473874,-852036,-917279,-216555,-814645,2147483645,-2147483648,2147483645,-814645,2147483645,-216555]
sol = Solution().singleNumber(nums)
print(sol)
