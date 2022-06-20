class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:

        # A method that partitions s into a valid word and recursively
        # calls itself to find a break on the rest of s.
        def get_word_break(s, wordDict_dict, start_idx, memo):

            # Termination condition: If start_idx is at the end, then
            # return True
            if start_idx == len(s):
                return True

            if start_idx in memo:
                return False

            # We will look for a break to partition out a valid word.
            # This partition will be a valid substring. For the other
            # partition, we recursively call get_word_break() method to
            # partition the rest of s into valid words. We keep trying
            # until we tried all the valid words w_dict in wordDict_dict.
            for w_dict in wordDict_dict.keys():

                # If word w_dict has been turned off, skip the rest of
                # the body and try the next word.
                if wordDict_dict[w_dict] is False:
                    continue

                # Calculate the stop_idx based on the length of w_dict
                stop_idx = start_idx + len(w_dict)

                # If stop_idx is out of bound, skip the rest of the body
                # and try the next word.
                if stop_idx > len(s):
                    continue

                # If s[start_idx:stop_idx] matches w_dict, then we try to see
                # if the rest of s: s[stop_index:len(s)], can also be broken
                # down into valid words. We do this by making a call to a
                # recursive function: get_word_break().
                if s[start_idx:stop_idx] == w_dict:

                    # Try to find if the rest of s is breakable.
                    breakable = get_word_break(s, wordDict_dict, stop_idx, memo)

                    # If it is, then we know s can be broken up into at least
                    # 2 valid words. Note that we also consider empty string ""
                    # as a valid word.
                    if breakable:
                        return True

            # If we have tried all the words in wordDict_dict and still could
            # not find a way to break s into valid words, then we return False
            # as it is impossible to break s into valid words.
            memo.add(start_idx)
            return False

        # Turn wordDict list into a dictionary for faster valid word lookup.
        wordDict_dict = {}
        for w in wordDict:
            wordDict_dict[w] = True

        # Simplify wordDict_dict by "turning off" words that can be further
        # broken down into smaller valid words in wordDict_dict. We will also
        # keep a memo of all the failed states. So that we don't have to waste
        # processing time to come to a failed conclusion again.
        memo = set()
        for w_dict in wordDict_dict.keys():

            # Turn off w_dict first.
            wordDict_dict[w_dict] = False

            # See if w_dict can be broken down into smaller valid words. If
            # it cannot be, then turn it back on.
            if get_word_break(w_dict, wordDict_dict, 0, memo) is False:
                wordDict_dict[w_dict] = True

        memo.clear()
        return get_word_break(s, wordDict_dict, 0, memo)


string ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
sol = Solution().wordBreak(string, dict)
print(sol)
