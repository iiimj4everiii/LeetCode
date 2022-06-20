class Solution:
    def numIslands(self, grid) -> int:

        from queue import Queue

        # Initialize island_count to 0.
        island_count = 0

        # We will use a queue to perform breadth-first search
        # through the graph.
        landmass = Queue()

        # Pad grid with one layer of '0' around it.
        new_grid = [['0' for _ in range(len(grid[0])+2)] for _ in range(len(grid)+2)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                new_grid[i+1][j+1] = grid[i][j]

        # Go through grid and perform BFS on elements that are
        # marked with '1'.
        for i in range(1, len(new_grid) - 1):
            for j in range(1, len(new_grid[0]) - 1):

                # If the current element is '1', do BFS to look
                # for landmasses, '1', that are connected to
                # the landmass at (i, j).
                if new_grid[i][j] == '1':

                    # Increase island_count by 1 since this is
                    # not part of any explored islands.
                    island_count += 1

                    # Enqueue landmass at (i, j) for BFS.
                    landmass.put([i, j])

                    # Turn (i, j) off so that we don't explore
                    # this same position again.
                    new_grid[i][j] = '0'

                    while not landmass.empty():
                        [r, c] = landmass.get()

                        if new_grid[r][c - 1] == '1':
                            new_grid[r][c - 1] = '0'
                            landmass.put([r, c - 1])

                        if new_grid[r - 1][c] == '1':
                            new_grid[r - 1][c] = '0'
                            landmass.put([r - 1, c])

                        if new_grid[r][c + 1] == '1':
                            new_grid[r][c + 1] = '0'
                            landmass.put([r, c + 1])

                        if new_grid[r + 1][c] == '1':
                            new_grid[r + 1][c] = '0'
                            landmass.put([r + 1, c])

        return island_count


grid = [
        ["1","0","1","1","1","0"]
]
sol = Solution().numIslands(grid)
print(sol)
