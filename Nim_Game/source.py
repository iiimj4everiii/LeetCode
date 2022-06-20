class Solution:
    def canWinNim(self, n: int) -> bool:
        
        # Initially, there is a heap of stones on the table.
        # You and your friend will alternate taking turns, and you go first.
        # On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
        # The one who removes the last stone is the winner.

        # Given n, the number of stones in the heap, return true if you can win the game
        # assuming both you and your friend play optimally, otherwise return false.

        # Strategy:
        # Notice that if there are 4 stones left, whoever goes next will always lose
        # assuming both players play optimally:
        # If player 1 removes 1, player 2 removes 3 and wins
        # If player 1 removes 2 instead, player 2 removes 2 and wins
        # If player 1 removes 3, player 2 removes 1 and wins
        # In fact if there are multiple of 4 stones left, the second player can force
        # the remaining number of stones on the table to be in multiple of 4's
        # until there are only 4 stones left

        return n % 4 != 0


print(Solution().canWinNim(10))
