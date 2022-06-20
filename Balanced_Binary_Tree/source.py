# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    balanced = True

    def isBalanced(self, root: TreeNode) -> bool:

        # Calculating depth is expensive.
        # This algorithm explores the deepest nodes first before calculating the depths.
        # Since unbalanced tree can happen at anytime, we keep a state variable "self.balanced".
        # We will only calculate children depths if they are balanced themselves.

        if root is None:
            return True

        # Check if the previous state is balanced
        if self.balanced:
            self.balanced = self.isBalanced(root.left)

        # Check if the left subtree is balanced
        if self.balanced:
            self.balanced = self.isBalanced(root.right)

        # Check if the right subtree is balanced
        if self.balanced:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)

            # Check if the height between left and right subtree depth differs by no more than 1.
            self.balanced = abs(left_depth - right_depth) <= 1

        return self.balanced

    def maxDepth(self, root: TreeNode) -> int:

        # If the current node is None, then return 0 depth
        if root is None:
            return 0

        # Otherwise, the dept is 1 + the max of the two subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


root = TreeNode(1)

# root.left = TreeNode(2)
# root.right = TreeNode(2)
#
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(3)

# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(4)

print(Solution().isBalanced(root))
