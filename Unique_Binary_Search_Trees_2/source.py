# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list:

        # Strategy:
        # We cannot use dynamic programming here as we need more than
        # just the number of trees that can be created with n number of
        # nodes.
        # 1) We will begin with various possible root positions.
        # 2) Get the list of all possible left subtrees beginning with
        #    start and ending with root position - 1.
        # 3) Get the list of all possible right subtrees beginning with
        #    root position + 1 and ending with stop.
        # 4) Use the given root position, left subtrees list and right
        #    subtrees list to generate all possible trees rooted at
        #    root_pos.
        # We do this for all possible root positions.

        return self.do_generate_trees(1, n)

    def do_generate_trees(self, start, stop):

        # Base case 1: If the start position is to the right of the stop
        # position, return [None] as this is impossible.
        if start > stop:
            return [None]

        # Base case 2: If the start position is the same as the stop
        # position, create a TreeNode with value = start and return it
        # inside a list.
        if start == stop:
            return [TreeNode(start)]

        # Otherwise, create an empty array to hold a list of trees of
        # size (stop - start) + 1.
        trees = []
        for root_pos in range(start, stop+1):

            # Recursively get the list of different left subtrees. The
            # value of the nodes in the left subtree should start with
            # start and ends with root_pos-1.
            left_subtrees = self.do_generate_trees(start, root_pos-1)

            # Similarly, recursively get the list of different right
            # subtrees. The value of the nodes in the right subtree should
            # start with root_pos+1 and ends with stop.
            right_subtrees = self.do_generate_trees(root_pos+1, stop)

            # Given a list of left_subtrees and a list of right subtrees, we
            # create len(left_subtrees) * len(right_subtrees) different trees
            # rooted at root_pos.
            self.create_trees(left_subtrees, right_subtrees, root_pos, trees)

        # Return the list of trees rooted at various root_pos.
        return trees

    # A helper method to create a list of trees for us given the:
    # 1) value of root node,
    # 2) A list of left subtrees,
    # 3) A list of right subtrees.
    @staticmethod
    def create_trees(left_subtrees, right_subtrees, root_val, trees):
        for ls in left_subtrees:
            for rs in right_subtrees:
                node = TreeNode(root_val)
                node.left = ls
                node.right = rs
                trees.append(node)


sol = Solution().generateTrees(3)
print(sol)
