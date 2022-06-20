# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:

        # Strategy:
        # To valid a Binary Search Tree, we will utilize one important fact about
        # BST: the nodes are sorted in order if we traverse the tree in-order. We
        # will base our algorithm on this fact. We traverse the tree in-order and
        # check for any ordering violations. If a violation is found, we return
        # False and stop going further into other branches of the tree.

        def in_order_traversal(node, prev_number):

            # Termination condition: if current node is None, return True
            if node is None:
                return True, prev_number

            # In-order traversal step 1: go left first. If we find a bad left
            # subtree, return False.
            left, prev_number = in_order_traversal(node.left, prev_number)
            if left is False:
                return False, prev_number

            # In-order traversal step 2: do something. Compare the previous number,
            # prev_number, with the current number, node.val. Since we are doing
            # in-order traversal on a Binary Search Tree, we should be processing
            # all the nodes in a sorted order. So if the prev_number is greater than
            # or equal to the current number, then we found a bad BST subtree.
            # Return False.
            center = True
            if prev_number is not None:
                if node.val <= prev_number:
                    return False, prev_number

            # Assign to prev_number our current number: node.val.
            prev_number = node.val

            # In-order traversal step 3: go right.
            right, prev_number = in_order_traversal(node.right, prev_number)

            # Return whatever we find after going right.
            return right, prev_number

        # Call the recursive function in_order_traversal to traverse into the BST
        # in-order. If there is an ordering violation during the tree traversal,
        # solution will be set to False. True, otherwise.
        solution, _ = in_order_traversal(root, None)

        return solution


r = TreeNode(2)
r.left = TreeNode(2)
r.right = TreeNode(2)
# r.right.left = TreeNode(3)
# r.right.right = TreeNode(7)
sol = Solution().isValidBST(r)
print(sol)
