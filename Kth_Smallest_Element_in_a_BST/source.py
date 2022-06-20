# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k: int) -> int:

        # Strategy:
        # Do inorder traversal of the tree. In this case, we do it
        # iteratively in order to be able to return early after
        # visiting k nodes.

        # The above recursion could be converted into iteration,
        # with the help of stack. This way one could speed up the
        # solution because there is no need to build the entire
        # inorder traversal, and one could stop after the kth element.

        stack = []
        curr = root
        while True:

            # Go all the way to the leftmost node where the deeper
            # nodes are on the top of the stack.
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            # Pop the deepest left node on the stack. This is similar
            # to finished exploring the left node.
            curr = stack.pop()

            # This is the do-something region in an in-order traversal.
            # In our case, we just returned from visiting a left node.
            # So we decrement k by 1 and check if k has reached 0. If
            # it did, then return the value in curr.
            k -= 1
            if k == 0:
                return curr.val

            # Visit the right node.
            curr = curr.right


r = TreeNode(5)

r.left = TreeNode(3)
r.right = TreeNode(6)

r.left.left = TreeNode(2)
r.left.right = TreeNode(4)

r.left.left.left = TreeNode(1)

sol = Solution().kthSmallest(r, 3)
print(sol)
