# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        # Strategy:
        # Traverse through all the nodes in the tree once
        # and exchange each node's left and right subtree pointers
        # Note: It is more natural to use pre-order or post-order traversal
        # In-order traversal is awkward because we swap after visiting one subtree
        # Then we will end up visiting the same subtree
        # since we swapped the left and right subtree after visiting one of them: e.g.
        # visit left, swap left <-> right, visit right. We ended up visiting left subtree twice

        # We will arbitrarily choose post-order tree traversal in this case

        # Termination condition
        if root is None:
            return None

        # Post-order tree traversal: visit left, visit right, do something
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Do something: swapping left and right pointer to subtrees
        root.left, root.right = root.right, root.left

        return root


root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

new_root = Solution().invertTree(root)

print()
