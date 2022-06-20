# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        # Handling corner cases
        if root is None:
            return False

        # The new_targetSum is the difference between the targetSum and current node's value
        new_targetSum = targetSum - root.val

        # If we hit a leaf node, check to see if the remainder targetSum is 0.
        if root.left is None and root.right is None:
            return new_targetSum == 0

        # Otherwise, check if the left subtree has a path sum equals to new_targetSum
        has_path_sum_left = False
        if root.left is not None:
            has_path_sum_left = self.hasPathSum(root.left, new_targetSum)

        # Check if the left subtree has a path sum equals to new_targetSum
        has_path_sum_right = False
        if root.right is not None:
            has_path_sum_right = self.hasPathSum(root.right, new_targetSum)

        return has_path_sum_left or has_path_sum_right


target_sum = 5

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

print(Solution().hasPathSum(None, target_sum))
