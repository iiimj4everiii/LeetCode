# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root) -> int:

        # Problem:
        # You are given the root of a binary tree containing digits
        # from 0 to 9 only. Each root-to-leaf path in the tree
        # represents a number.
        # For example, the root-to-leaf path 1 -> 2 -> 3 represents
        # the number 123.
        # Return the total sum of all root-to-leaf numbers. Test cases
        # are generated so that the answer will fit in a 32-bit integer.

        # A path sum function that recursively call itself until we
        # get to a valid root-to-leaf path or root-to-None path. In
        # the former case, we return the new num. In the latter case,
        # we return 0 since it is not a valid root-to-leaf path.
        def get_path_num(root, old_num):
            # Not a valid root-to-leaf (node with no children) path.
            # Therefore, return 0 for path sum.
            if root is None:
                return 0

            # For the new num, the value is calculated by multiplying
            # the old num by 10, then add to it the current root's value.
            new_num = old_num * 10 + root.val

            # If this node is a leaf node, we return the new num.
            if root.left is None and root.right is None:
                return new_num

            # Otherwise, we try going deeper left and deeper right until
            # we get to a leaf node.
            left = get_path_num(root.left, new_num)
            right = get_path_num(root.right, new_num)

            return left + right

        return get_path_num(root, 0)


r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)

sol = Solution().sumNumbers(r)
print(sol)
