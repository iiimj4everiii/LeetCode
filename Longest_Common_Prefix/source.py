class Solution:
    def longestCommonPrefix(self, strs) -> str:

        # Corner case 1
        if len(strs) == 0:
            return ''

        # Corner case 2
        if len(strs) == 1:
            return strs[0]

        # List of string length
        lens = [len(x) for x in strs]

        # The shortest string length
        min_len = min(lens)

        # Iterate through each string and compare them letter by letter
        # starting from the 0th index
        for i in range(min_len):
            for s in strs[1:]:

                # If we find a mismatch, then we are done
                if not s[i] == strs[0][i]:
                    return s[:i]

        return strs[0][:min_len]

strs = ["ab", "a"]

print(Solution().longestCommonPrefix(strs))
