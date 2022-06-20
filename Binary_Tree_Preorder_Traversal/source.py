# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversal(self, root: TreeNode):

        # The preorder traversal node list
        traversal_list = []

        self.do_preorder_traversal(root, traversal_list)

        return traversal_list

    # Preorder traversal:
    # 1) Do something
    # 2) Visit left subtree
    # 3) Visit right subtree
    def do_preorder_traversal(self, root, traversal_list):

        # Termination condition
        if root is None:
            return

        # Step 1)
        traversal_list.append(root.val)

        # Step 2)
        self.do_preorder_traversal(root.left, traversal_list)

        # Step 3)
        self.do_preorder_traversal(root.right, traversal_list)

        return


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(Solution().preorderTraversal(root))
