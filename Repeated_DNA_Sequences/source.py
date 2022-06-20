class Solution:
    def findRepeatedDnaSequences(self, s: str):

        # Strategy:
        # Go through s and see if we saw seq = s[i:i+10]
        # already before. If we saw it before, add it to
        # res_set. Otherwise, add it to the visited set.
        # At the end convert res_set to a list and return.

        # Handling corner cases
        if len(s) < 10:
            return []

        # Initialize visited and res_set to empty sets.
        visited = set()
        res_set = set()

        # Go through s and see if we saw seq = s[i:i+10]
        # already before. If we saw it before, add it to
        # res_set. Otherwise, add it to the visited set.
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq in visited:
                res_set.add(seq)
            else:
                visited.add(seq)

        # Convert res_set to a list and return.
        return list(res_set)


string = "AAAAAAAAAAA"
sol = Solution().findRepeatedDnaSequences(string)
print(sol)
