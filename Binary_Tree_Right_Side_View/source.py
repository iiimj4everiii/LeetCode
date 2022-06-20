# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):

        from queue import Queue

        # Corner cases: if root is None, return an empty list.
        if root is None:
            return []

        # Initialize res to an empty list.
        res = []

        # Initialize q to root and node_counts to 1.
        q = Queue()
        q.put(root)
        node_counts = 1

        # We keep traversing through the tree in-order as long
        # as there are nodes in q.
        while node_counts > 0:

            for i in range(node_counts):

                # Dequeue from q and push its children to q if
                # they are not None.
                node = q.get()

                if node.left is not None:
                    q.put(node.left)

                if node.right is not None:
                    q.put(node.right)

                # If we are at the last node in the current tree
                # level, add its value to res. This is our right-
                # most node at the current level.
                if i == node_counts - 1:
                    res.append(node.val)

            # Update node_counts to the number of nodes enqueued
            # onto q.
            node_counts = len(q.queue)

        return res


r = TreeNode(5)

r.left = TreeNode(4)
r.right = TreeNode(6)

r.left.left = TreeNode(1)
r.left.right = TreeNode(3)
r.right.right = TreeNode(101)

r.left.left.left = TreeNode(0)
r.left.left.right = TreeNode(2)
r.left.right.left = TreeNode(100)

sol = Solution().rightSideView(r)
print(sol)
