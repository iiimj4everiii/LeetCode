class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Remove leading and trailing white spaces
        s = s.strip()

        for i in reversed(range(len(s))):
            if s[i] == ' ':
                return len(s)-i-1

        return len(s)


s = " "
print(Solution().lengthOfLastWord(s))
