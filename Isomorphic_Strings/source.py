class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Strategy: Go through s and t letter by letter
        # Create a dictionary of key/value (si/ti) mapping for every unseen letter in s
        # If we find a mapping that contradicts with the ones in the dictionary, or different
        # keys are mapped to the same value, then we know s and t are not isomorphic.

        # Quick a dirty way of detecting false isomorphic
        if len(s) != len(t):
            return False

        # Keep a dictionary of all the letter mapping found so far
        # as we iterate through string s(keys) and t(values)
        s_to_t_mapping = {}

        # At this point, the string length for s and t are equal
        # We iterate through string s and t
        for si, ti in zip(s, t):

            # If we already have a letter mapped to key si but the value ti
            # does not match our record, then s and t are not isomorphic
            if si in s_to_t_mapping:
                if s_to_t_mapping[si] != ti:
                    return False

            # Or, if this is the first time we are seeing key si but value ti has already
            # been mapped to a different key, then s and t are also not isomorphic
            if si not in s_to_t_mapping:
                if ti in s_to_t_mapping.values():
                    return False

                # Otherwise, add the key to the dictionary and map to value ti
                else:
                    s_to_t_mapping[si] = ti

        # If we have gotten through all the letters in s and t without detecting
        # false isomorphic, then we know s and t are isomorphic
        return True


print(Solution().isIsomorphic("paper", "title"))
