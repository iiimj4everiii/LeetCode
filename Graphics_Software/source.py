# There are 3 types of edits on a string
# 1) Insert character
# 2) Remove a character
# 3) Replace a character

# Given 2 strings,

# String 1 = pale
# String 2 = ple

# a le
#  le

# p
# el

# def compare_str(str1: str, str2: str):
#
#     # This ensures str1 and str2 is no more than 1 letter in length apart
#     if abs(len(str1) - len(str2)) > 1:
#         return False
#
#     # Goes from left to right
#     from_left_index = 0
#     for s1, s2 in zip(str1, str2):
#         if s1 != s2:
#             break
#         from_left_index += 1
#
#     # Goes from right to left
#     from_right_index = 0
#     for s1, s2 in zip(reversed(str1[from_left_index:]), reversed(str2[from_left_index:])):
#         if s1 != s2:
#             break
#         from_right_index += 1
#
#     return (from_left_index + from_right_index + 1) >= max(len(str1), len(str2))
#
#
# print(compare_str("pale", "ple"))
# print(compare_str("pale", "bae"))
# print(compare_str("pales", "pale"))
# print(compare_str("pale", "bale"))

# swap odd and even bit of an integer
# input: 0111 0101
# odd mask:  1010 1010
# even mask: 0101 0101

# input:     0111 0101
# odd mask:  1010 1010
# res1 = 0010 0000
# res2 = shift res1 1 bit to right
# 0001 0000

# input:     0111 0101
# even mask: 0101 0101
# res3 = 0101 0101
# res4 = shift res2 1 bit to left
# 1010 1010

#finally, I add res4 to res2
# return: 1011 1010
# input:  0111 0101


def swap(num: int):
    odd_mask = 0xAAAAAAAA
    even_mask = 0x55555555

    res_odd = odd_mask & num
    res_even = even_mask & num

    res_odd = res_odd >> 1
    res_even = res_even << 1

    # 0111 1111
    assert(res_odd + res_even > 0x7AAAAAAA)

    return res_odd + res_even


print(swap(117))
