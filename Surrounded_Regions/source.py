class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Problem:
        # Given an m x n matrix board containing 'X' and 'O', capture all
        # regions that are 4-directionally surrounded by 'X'.
        # A region is captured by flipping all 'O's into 'X's in that
        # surrounded region.

        # Strategy:
        # Find all the 'O' marked nodes around the outer border. These
        # will be our starting nodes. Then use BFS to search all the nodes
        # that are directly adjacent to these starting nodes and all the
        # nodes that are directly adjacent to those directly-adjacent-nodes
        # and etc.

        # We will use Breadth-First-Search method to find all the nodes that
        # are horizontally/vertically connected a 'O', starting from root.
        def BFS(board, root, height, width):

            # A homemade queue data structure class.
            class Queue:

                head = None
                tail = None

                class ListNode:
                    def __init__(self, val=0, next=None):
                        self.val = val
                        self.next = next

                def __init__(self, val=None):
                    self.head = self.ListNode(val)
                    self.tail = self.head

                def enqueue(self, val):
                    if self.head is None:
                        self.__init__(val)
                    else:
                        self.tail.next = self.ListNode(val)
                        self.tail = self.tail.next

                def dequeue(self):
                    val = self.head.val
                    self.head = self.head.next

                    if self.head is None:
                        self.tail = None

                    return val

                def empty(self):
                    return self.head is None

            # Get the horizontal and vertical direct neighbors of (rr, rc)
            def neighborhood(r, c):
                return [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]

            # Return True if the neighbor is within inner bound.
            def valid_neighbor(neighbor, height, width):

                valid_row = 0 < neighbor[0] < height-1
                valid_col = 0 < neighbor[1] < width-1

                return valid_row and valid_col

            # Do breadth-first-search on root.
            q = Queue(root)
            while not q.empty():
                node = q.dequeue()
                # Expand and explore the neighborhood of node.
                for neighbor in neighborhood(node[0], node[1]):
                    # Add neighbor to queue if the neighbor is within the
                    # inner bound and neighbor is marked with 'O'.
                    if valid_neighbor(neighbor, height, width):
                        if board[neighbor[0]][neighbor[1]] == 'O':
                            q.enqueue(neighbor)
                            board[neighbor[0]][neighbor[1]] = 'V'

            return None

        # Get the height and width of the board
        height = len(board)
        width = len(board[0])

        # Handling corner cases. If either height or width is less than
        # 3, we don't have to do anything because all the nodes are outer
        # border nodes.
        if height < 3 or width < 3:
            return

        # Initialize roots to an empty list. roots will hold all the 'O'
        # marked nodes on the outer/surrounding border of board.
        roots = []

        # Get the roots on the top outer border.
        for i in range(width-1):
            if board[0][i] == 'O':
                roots.append((0, i))

        # Get the roots on the right outer border.
        for i in range(height-1):
            if board[i][width-1] == 'O':
                roots.append((i, width-1))

        # Get the roots on the bottom outer border.
        for i in reversed(range(width-1)):
            if board[height-1][i] == 'O':
                roots.append((height-1, i))

        # Get the roots on the left outer border.
        for i in reversed(range(height-1)):
            if board[i][0] == 'O':
                roots.append((i, 0))

        # Process all the roots in roots list. After all the roots
        # are processed, all the non-surrounded nodes will be marked
        # with 'V' and all the surrounded nodes will be left as 'O'
        for r in roots:
            BFS(board, r, height, width)

        # Go through all the nodes in the inner border. If a node is
        # marked 'O', change it to 'X'. If a node is marked 'V',
        # change it to 'O'. All the 'X' marked nodes will be left alone.
        for i in range(1, height-1):
            for j in range(1, width-1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == 'V':
                    board[i][j] = 'O'

        return None


b = [
    ['X','O','X','X']
]
Solution().solve(b)
print(b)
