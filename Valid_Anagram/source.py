class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Strategy:
        # Keep a dictionary of letter counts of either string s or t
        # Then loop through t/s and decrement the letter count in the
        # dictionary of that character/letter.
        # If we cannot decrement a letter from the dictionary, that means
        # s and t are not a anagram

        # If the string lengths are different between s and t,
        # then we know they cannot be an anagram
        if len(s) != len(t):
            return False

        # A dictionary to hold character counts in string s
        s_dict = {}
        for si in s:
            # If key si exists, increment its count by 1
            if si in s_dict.keys():
                s_dict[si] += 1
            # Otherwise, set its value to 1
            else:
                s_dict[si] = 1

        # At this point, we have a dictionary of letter counts of string s
        # Now we will go through each letter in string t and see if t has
        # all the letters and their counts as in string s
        for ti in t:

            # If key ti does not exist in s_dict, then we know s and t are not anagram
            if ti not in s_dict.keys():
                return False

            # If the count of letter ti is already at 0, we know t contains at least
            # 1 extra count of letter ti than s. Return False
            if s_dict[ti] == 0:
                return False

            # Otherwise, decrement the count of letter ti by 1
            s_dict[ti] -= 1

        # At this point, all the letters in string s can pair up nicely
        # with all the letters in string t. Therefore s and t are an anagram.
        return True


print(Solution().isAnagram("car", "rat"))
