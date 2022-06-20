# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode):

        # The preorder traversal node list
        traversal_list = []

        self.do_postorder_traversal(root, traversal_list)

        return traversal_list

    # Postorder traversal:
    # 1) Visit right subtree
    # 2) Do something
    # 3) Visit left subtree
    def do_postorder_traversal(self, root, traversal_list):

        # Termination condition
        if root is None:
            return

        # Step 1)
        self.do_postorder_traversal(root.left, traversal_list)

        # Step 2)
        self.do_postorder_traversal(root.right, traversal_list)

        # Step 3)
        traversal_list.append(root.val)

        return


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(Solution().postorderTraversal(root))
