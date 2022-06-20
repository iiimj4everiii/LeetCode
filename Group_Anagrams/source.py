class Solution:
    def groupAnagrams(self, strs: list) -> list:

        # Strategy:
        # We will use a list of alphabet counts to count the occurrence of each
        # letter in each string in strs list. We will convert this list of
        # alphabet counts to a tuple for hashing purpose. We create a dictionary
        # to map the alphabet counts to an index in the solution list that
        # contains a list of strings that are an anagram. A string is an anagram
        # of the other if they have the same alphabet counts. Our dictionary will
        # give us the index location of the anagram string list within solution
        # list. We can append our current string to this anagram string list. If
        # the alpha_count tuple of a string does not exist in our dictionary, that
        # means, this string is in a different anagram family. A new entry of
        # dictionary will be created mapping to a new index in solutions list.

        # Get the alphabet counts of string. Return the TUPLE of alphabet counts
        # of every letter in string where:
        # 'a' is mapped to index 0,
        # 'b' is mapped to index 1,
        # ...
        # 'z' is mapped to index 25
        # We are returning a tuple so that later on we can use these tuples
        # for hashing.
        def get_alpha_count(string) -> tuple:

            # Create a list and initialize all alphabet count to 0.
            alpha_count = [0] * 26

            # Integer representation of 'a' in ASCII is 97.
            ASCII_OFFSET = 97

            # For each letter s in string, get the integer presentation of the
            # letter in ASCII and offset it by 97 (ASCII_OFFSET). This will be
            # mapped to a list of alphabet counts starting at index 0. Increment
            # that letter count by 1.
            for s in string:
                index = ord(s)-ASCII_OFFSET
                alpha_count[index] += 1

            return tuple(alpha_count)

        # Initialize solution to an empty list.
        solution = []

        # Dictionary that maps alpha_count to the index of the anagram list
        # within the solution list.
        alpha_count_to_anagram_index = {}

        # Iterate through all the indices of strs list.
        for i in range(len(strs)):

            # Get the alphabet counts TUPLE of the ith string in strs.
            # The reason why we are returning a tuple is because we will use
            # these alphabet counts as hashable keys for
            # dictionary (alpha_count_to_anagram_index) lookup.
            alpha_count = get_alpha_count(strs[i])

            # If alpha_count tuple is already a key in alpha_count_to_anagram_index
            # dictionary, get the anagram index and append the ith string in strs
            # to the anagram list in anagram_idx location.
            if alpha_count in alpha_count_to_anagram_index.keys():
                anagram_idx = alpha_count_to_anagram_index[alpha_count]
                solution[anagram_idx].append(strs[i])

            # Otherwise, create a new entry in alpha_count_to_anagram_index and assign
            # a value of len(solution) to it. Then append [strs[i]] to solution list.
            else:
                alpha_count_to_anagram_index[alpha_count] = len(solution)
                solution.append([strs[i]])

        return solution


# s = ["eat","tea","tan","ate","nat","bat"]
# sol = Solution().groupAnagrams(s)
# print(sol)

s = set()
s.add(())
