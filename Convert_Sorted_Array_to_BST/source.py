# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:

        # Find the middle index of nums array
        mid_idx = len(nums) // 2

        # Construct a TreeNode with the value of nums[mid_idx]
        root = TreeNode(nums[mid_idx])

        # Extract the left subarray of nums
        # Recursively build left subtree
        left_subarray = nums[:mid_idx]
        if len(left_subarray) > 0:
            root.left = self.sortedArrayToBST(left_subarray)

        # Extract the right subarray of nums
        # Recursively build right subtree
        right_subarray = nums[mid_idx+1:]
        if len(right_subarray) > 0:
            root.right = self.sortedArrayToBST(right_subarray)

        return root


l = [0,1,2,3,4,5,6]
node = Solution().sortedArrayToBST(l)

print()
