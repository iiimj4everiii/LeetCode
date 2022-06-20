class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False


class WordDictionary:

    # Strategy:
    # Our data structure will be similar to a Trie (Prefix tree)
    # data structure. The constructor will be the same. Method
    # addWord() will be the same as method insert() of Trie. The
    # only difference will be the search() method. Instead of
    # going through word:str iteratively (as in Trie), we will
    # search through our data structure recursively as we might
    # need to step back and explore different part of the tree.

    # Same as __init__() of Trie data structure.
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    # Same as insert() of Trie data structure.
    def addWord(self, word: str) -> None:
        if len(word) == 0:
            return None

        curr = self.root
        for w in word:

            if w not in curr.children.keys():
                curr.children[w] = TrieNode()

            curr = curr.children[w]

        curr.terminal = True

        return None

    # Instead of going through word:str iteratively (as in Trie),
    # we will search through our data structure recursively as
    # we might need to step back and explore different part of
    # the tree.
    def search(self, word: str) -> bool:

        def dfs_search(curr, word, idx) -> bool:

            # Base case: if the last letter has terminal = True,
            # then word:str exists in our data structure.
            if idx == len(word):
                return curr.terminal

            # Get the word's letter at index = idx. This is our
            # key for current TrieNode's children:dict
            key = word[idx]

            # If key happens to be a special key = '.',
            if key == '.':

                # we will explore every child:TrieNode in
                # children:dict.
                for child in curr.children.values():

                    # we will recursively call dfs_search to
                    # explore every child in children:dict. If
                    # word:str exists in our data structure,
                    # dfs_search() will return True. We pass this
                    # fact to the caller by returning True.
                    if dfs_search(child, word, idx+1):
                        return True

            # If key is not one of curr's children's key, then we
            # know word:str does not exist in our data structure.
            # Return False to the caller.
            elif key not in curr.children.keys():
                return False

            # Otherwise, go to the child node mapped to key and
            # explore deeper.
            else:
                curr = curr.children[key]
                return dfs_search(curr, word, idx+1)

            return False

        return dfs_search(self.root, word, 0)


# Your WordDictionary object will be instantiated and called as such:
D = WordDictionary()
D.addWord("bad")
D.addWord("dad")
D.addWord("mad")
D.addWord("mom")
print(D.search("pad"))
print(D.search("bad"))
print(D.search(".ad"))
print(D.search("b.."))
print(D.search("m.m"))
