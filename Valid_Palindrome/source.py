class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Initialize formatted s and formatted s reversed to ''
        s_formatted = ''

        # For each letter in s, append the alpha-numeric letter to s_formatted
        for si in s:
            if si.isalnum():
                s_formatted = s_formatted + si.lower()

        return s_formatted[::-1] == s_formatted


print(Solution().isPalindrome("0p"))
