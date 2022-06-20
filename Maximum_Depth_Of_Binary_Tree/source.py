# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        # If the current node is None, then return 0 depth
        if root is None:
            return 0

        # Otherwise, the dept is 1 + the max of the two subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    root = TreeNode(3)

    # root.left = TreeNode(9)

    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)

    print(Solution().maxDepth(root))
