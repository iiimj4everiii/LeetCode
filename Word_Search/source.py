class Solution:

    m = 0
    n = 0
    word = ''
    word_len = 0

    def exist(self, board: list, word: str) -> bool:

        # Get the size of board.
        self.m = len(board)
        self.n = len(board[0])
        self.word = word
        self.word_len = len(word)

        # This is our main work function. This function will explore the letter at the
        # current location (r, c). If this letter is the same as the letter in
        # word[word_idx], then we explore deeper until we get to the termination
        # condition.
        def sub_exist(board: list, word_idx: int, r: int, c: int, taken: set) -> bool:

            # Termination condition: if word_idx is the last index of word, return
            # True if the letter at the current location (r, c) is the same as
            # self.word[word_idx]. False otherwise.
            if word_idx == self.word_len - 1:
                return board[r][c] == self.word[word_idx]

            # Otherwise, see if the letter in the current board position (r, c) is the
            # same as the letter in word[word_idx]. If that is True, explore deeper.
            if board[r][c] == self.word[word_idx]:

                # we will take this letter and add this index to taken set.
                taken.add((r, c))

                # Then we get all the valid neighbors. Recursively search for the next
                # letter in word.
                for n in self.get_neighbors(r, c, taken):

                    # If sub_word exists somewhere down the rabbit hole, we return True
                    if sub_exist(board, word_idx+1, n[0], n[1], taken):
                        return True

                # At this point, we have explored all the neighbors and none of them is
                # a part of word. Therefore letter at index (r, c) does not lead to a
                # valid solution. Remove it from the set and return False.
                taken.remove((r, c))

            return False

        # Initialize taken to an empty set. Taken will keep track of all the indices
        # that currently makes up a substring of word. This will be used to find
        # valid neighbors for the next letter in word.
        taken = set()

        # The main loop that goes through the entire board and calls the main work
        # work function that explores the the letter in position (r, c) and then
        # recursively explores its neighbors if letter in position (r, c) is same
        # as the first letter of word.
        for r in range(self.m):
            for c in range(self.n):

                # If word exists somewhere down  in the rabbit hole, we return True.
                if sub_exist(board, 0, r, c, taken):
                    return True

        return False

    # Get all the indices of all un-taken neighbors (in tuple format).
    def get_neighbors(self, r: int, c: int, taken: set) -> list:

        # Initialize neighbors_set as a set.
        neighbors_set = set()

        # Add all "potential" neighbors to the set.
        neighbors_set.add((r, c+1))
        neighbors_set.add((r+1, c))
        neighbors_set.add((r, c-1))
        neighbors_set.add((r-1, c))

        # If we are at the 0th row, we know row r-1 is not possible.
        # Remove it from the set.
        if r == 0:
            neighbors_set.remove((r-1, c))

        # If we are at the (self.m-1)th row, we know row r+1 is not possible.
        # Remove it from the set.
        if r == self.m-1:
            neighbors_set.remove((r+1, c))

        # If we are at the 0th column, we know column c-1 is not possible.
        # Remove it from the set.
        if c == 0:
            neighbors_set.remove((r, c-1))

        # If we are at the (self.n-1)th column, we know column c+1 is not
        # possible. Remove it from the set.
        if c == self.n-1:
            neighbors_set.remove((r, c+1))

        # Initialize neighbors to an empty list.
        neighbors = []

        # For whatever that is left in the neighbors_set,
        for n in neighbors_set:

            # if neighbor n is not taken yet, n is a valid candidate for
            # the next letter in word. Add it to neighbors list.
            if n not in taken:
                neighbors.append(n)

        return neighbors


# b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
b = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
sol = Solution().exist(b, "ABCESEEEFS")
print(sol)
