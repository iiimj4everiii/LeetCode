class Solution:
    def singleNumber(self, nums: list) -> list:

        # We xor all the numbers in nums in order to filter out all
        # the matching pairs. Since there are 2 (not 1) unique numbers,
        # the result of xor-ing all the numbers in nums will be the
        # result of xor-ing just the 2 unique numbers: num0 and num1.
        xor_all = 0
        for n in nums:
            xor_all = xor_all ^ n

        # In order to separate num1 and num2 from xor_all, we need
        # something to filter them apart.
        # INSIGHT:
        # We know that xor_all cannot be 0 because that implies that
        # num0 == num1. Since we know that num0 =/= num1, there must
        # be at least one bit that is different between these 2
        # numbers. We will call this bit mask_bit. CONCEPTUALLY, We
        # will break nums into 2 groups/lists: a list with all the
        # numbers in nums with their mask bit = 0 and a list with all
        # the numbers in nums with their mask bit = 1.

        mask_bit = self.get_mask_bit(xor_all)

        # We will xor all the numbers in nums with their mask_bit = '1'.
        # EFFECTIVELY, this will pull out all the numbers with their
        # mask_bit = 1 INCLUDING THE 1 UNIQUE NUMBER WITH MASK_BIT = 1.
        # The result from this operator will give us 1 of the unique
        # number: the one with '1' in its' mask bit.
        num1 = 0
        for n in nums:
            bin_n = bin((1 << 32) - n)[2:]
            if bin_n[-(mask_bit+1)] == '1':
                num1 = num1 ^ n

        # To get the other unique number: one with '0' in its' mask bit,
        # all we have to do is xor xor_all with num1. This is because of:
        # num0 ^ num1 = xor_all
        # num0 ^ num1 ^ num1 = xor_all ^ num1
        # num0 ^ 0 = xor_all ^ num1
        # num0 = xor_all ^ num1
        num0 = xor_all ^ num1

        return [num0, num1]

    @staticmethod
    # This method will return the mask_bit of xor_all. We do this by
    # searching for '1', bit by bit, starting from the right hand side.
    def get_mask_bit(xor_all):

        mask_bit = 0
        bin_xor_all = bin((1 << 32) - xor_all)[2:]
        while bin_xor_all[-(mask_bit + 1)] == '0':
            mask_bit += 1

        return mask_bit


main_nums = [-1,2,-1,3,2,-5]
sol = Solution().singleNumber(main_nums)
print(sol)
