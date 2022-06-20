# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root):

        traversal_list = []

        return self.do_inorder_traversal(root, traversal_list)

    def do_inorder_traversal(self, node, traversal_list):

        # Recursion termination condition
        if node is None:
            return None

        # Inorder traversal:
        # 1) Go left
        # 2) Come back from left, do something special
        # 3) Go right
        self.do_inorder_traversal(node.left, traversal_list)
        traversal_list.append(node.val)
        self.do_inorder_traversal(node.right, traversal_list)

        return traversal_list


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(Solution().inorderTraversal(root))
