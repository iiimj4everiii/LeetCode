# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum):

        # Problem:
        # Given the root of a binary tree and an integer targetSum,
        # return all root-to-leaf paths where the sum of the node values
        # in the path equals targetSum. Each path should be returned as a
        # list of the node values, not node references.

        # Strategy:
        # We find the path sum by recursively call get_path_sum method to
        # find the updated target sum (target_sum - root.val) in the left
        # and right subtree. When we recurse to a leaf node (node with 2
        # NoneType as children), we check if target_sum - root.val = 0. If it
        # is, then we found a path from root to leaf that sums to targetSum.
        # Append the last root.val to a potential solution list and append it
        # to the solution list.

        def get_path_sum(solution, potential_sol, root, target_sum):

            # Termination condition 1: if we reach a NoneType node, just return.
            if root is None:
                return

            # Termination condition 2: if we reach a leaf node,
            if root.left is None and root.right is None:

                # check if target_sum - root.val = 0. If it is, append root.val
                # to potential_sol. Create a copy of potential_sol and append it
                # to solution list. Pop out root.val from potential_sol and
                # return to the parent.
                if root.val == target_sum:
                    potential_sol.append(root.val)
                    sol = list(potential_sol)
                    solution.append(sol)
                    potential_sol.pop(-1)

                return

            # Append root.val to potential_sol.
            potential_sol.append(root.val)

            # Recursively find the path sum of the new target_sum in the left
            # subtree.
            get_path_sum(solution, potential_sol, root.left, target_sum - root.val)

            # Likewise, recursively find the path sum of the new target_sum in
            # the right subtree.
            get_path_sum(solution, potential_sol, root.right, target_sum - root.val)

            # Pop out root.val from potential_sol and return to the parent.
            potential_sol.pop(-1)
            return

        # Initialize solution to an empty list. This will hold the value of all
        # the nodes from root to leaf that sums to targetSum.
        solution = []

        # Call get_path_sum to get the solution of paths that sum to targetSum.
        get_path_sum(solution, [], root, targetSum)

        return solution


r = TreeNode(5)

r.left = TreeNode(4)
r.right = TreeNode(8)

r.left.left = TreeNode(11)
r.right.left = TreeNode(13)
r.right.right = TreeNode(4)

r.left.left.left = TreeNode(7)
r.left.left.right = TreeNode(2)
r.right.right.left = TreeNode(5)
r.right.right.right = TreeNode(1)

sol = Solution().pathSum(r, 27)
print(sol)
