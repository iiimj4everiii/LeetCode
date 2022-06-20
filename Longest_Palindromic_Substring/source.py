class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Strategy (this implementation):
        # Reverse the string s and append char in s to current_string.

        # If current_string does not exist in reverse, then we remove the char in
        # current_string, one at a time, from the left until current_string exists in reverse.

        # If current_string exists in reverse, then we know that current_string
        # could be a palindrome. We check it be comparing current_string
        # with the reversed version of itself. If current_string is a valid palindrome,
        # compare it with the longest_palindrome. Update it if current_string is longer.

        # Strategy #2:
        # Manacher's algorithm.
        # https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm

        # Reverse the string s
        reverse = s[::-1]

        # Initialize longest_palindrome and current_string to empty string
        longest_palindrome = ''
        current_string = ''

        # For each char in s, append char to the current_string. If current_string is not a substring
        # of reverse, we remove character at a time from the left side of the current_string until
        # the current_string becomes a substring of reverse.
        # Finally, we check if the current_string is longer than the longest_palindrome
        # and is also a valid palindrome. Update the longest_palindrome if current_string is longer.
        for char in s:
            current_string += char

            while reverse.find(current_string) < 0:
                current_string = current_string[1:]

            if len(current_string) > len(longest_palindrome) and current_string == current_string[::-1]:
                longest_palindrome = current_string

        return longest_palindrome


print(Solution().longestPalindrome("babad"))
