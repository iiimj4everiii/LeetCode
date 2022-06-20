class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        # Strategy:
        # We iterate through the characters in s and keeping track of the characters encountered.
        # If the new char is not in the current_substring, we add the new char to it.

        # Otherwise, we arrived at the end of the current_substring. Compare the length of the
        # current_substring to the longest_substr_length. Update it if current_substring is longer.
        # Then we find the index of the first occurrence of the duplicate char and splice out the
        # right-side part of the current_substring (starting from index + 1).
        # Finally, add the new char to the current_substring

        # Initialize the longest substring length to be 0
        longest_substr_length = 0

        # Initialize the current substring to be ''
        current_substring = ''

        # For every character in string s, see if the char is already in the current_substring
        for char in s:

            # If char is already in the current_substring, update the longest_substr_length if longer,
            # find the index of the first occurrence of the duplicate char,
            # and splice out the right-side part of the current_substring (starting from index + 1)
            if char in current_substring:
                longest_substr_length = max(longest_substr_length, len(current_substring))
                index = current_substring.find(char)
                current_substring = current_substring[index+1:]

            # Add the current char to the current_substring
            current_substring += char

        # Finally return the max of longest_substr_length or the current_substring length
        return max(longest_substr_length, len(current_substring))


print(Solution().lengthOfLongestSubstring('dvdf'))
