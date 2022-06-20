class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # Strategy:
        # We create a pattern : word dictionary
        # If there is any contradiction to the pattern : word,
        # then we don't have a valid word pattern.
        # A contradiction can be: 2 different patterns mapped to the same word
        # Or 1 pattern mapped to 2 different words.

        # A quick way to see if pattern cannot be matched to s
        # NOTE: the split() method extracts all the words from a string of words
        if len(pattern) != len(s.split()):
            return False

        # Initialize a pattern:word dictionary lookup table and a set of all the paired up words
        pattern_dict = {}
        words_paired = set()

        # for each key/value (p/word) pair, check to see
        # if key p already exist in the pattern_dict. If it is,
        # check to see if the new word matches what p had been paired up with
        # If the new word matches the old word, then we are good. Otherwise, return False
        # If key p does not exist, check to see if the word has already been paired up with another key
        # If the word has already been paired with another key, then return False.
        # Otherwise, add word to words_paired set and add the p:word to the pattern_dict
        for p, word in zip(pattern, s.split()):

            # Check to see if key p already exist in the pattern_dict
            if p not in pattern_dict:

                # Check to see if the word has already been paired up with another key
                # If the word has already been paired with another key, return False
                if word in words_paired:
                    return False

                # Otherwise, add word to words_paired set and add the p:word to the pattern_dict
                pattern_dict[p] = word
                words_paired.add(word)

            else:
                # Check to see if the new word matches what p had been paired up with
                if pattern_dict[p] != word:
                    return False

        # If we did not find any contradictions, then we have a valid word pattern
        return True


print(Solution().wordPattern("abba", "cat dog dog cat"))
