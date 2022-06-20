# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q) -> bool:

        return self.dual_inorder_traversal(p, q)

    def dual_inorder_traversal(self, p, q):

        # Recursion termination condition 1
        if p is None and q is None:
            return True

        # Recursion termination condition 2
        elif p is None and q is not None:
            return False

        # Recursion termination condition 3
        elif p is not None and q is None:
            return False

        else:
            # Inorder traversal:
            # 1) Go left
            # 2) Come back from left, do something special
            # 3) Go right
            if self.dual_inorder_traversal(p.left, q.left) and p.val == q.val and self.dual_inorder_traversal(p.right, q.right):
                return True
            return False

p = TreeNode(1)
p.left = TreeNode(1)

q = TreeNode(1)
q.left = TreeNode(1)

print(Solution().isSameTree(None, None))
