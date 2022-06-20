# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Problem:
        # Given the root of a binary tree, flatten the tree into a "linked list":
        # - The "linked list" should use the same TreeNode class where the right
        #   child pointer points to the next node in the list and the left child
        #   pointer is always null.
        # - The "linked list" should be in the same order as a pre-order traversal
        #   of the binary tree.

        # Strategy:
        # Recursive restructure the tree starting from the deepest left node.
        # 1) We want to keep track of the last node we can get to in the current
        # subtree in a pre-order faction. We return this last node to the caller.
        # 2) After we return to the caller, we want to take the caller's right subtree
        # and attach it to the last node's right subtree (The last node's right subtree
        # should always be a nullptr).
        # 3) Point the caller's right to the caller's left subtree.
        # 4) Point the caller's left to a nullptr.
        # 5) Finally move root node to last node's position.
        # If the new root node's right (last node's right) is not None, we recurse
        # right. Our termination condition is when we get to a leaf node (only NoneType
        # children). In that case, we simply return this leaf node to the caller.

        def do_flattening(sub_root) -> TreeNode:

            last_node = sub_root

            # If sub_root is not a leaf node (left subtree is not None),
            if sub_root.left is not None:

                # we recurse deeper into the left subtree.
                last_node = do_flattening(sub_root.left)

                # When we come back from a left subtree, we should have a pointer to
                # last_node, the deepest node in that left subtree (in a pre-order
                # faction). We start the restructuring process:
                # 1) Attach sub_root's right subtree to last_node's right subtree
                # 2) Point sub_root's right to sub_root's left subtree.
                # 3) Point sub_root's left to a nullptr.
                last_node.right = sub_root.right
                sub_root.right = sub_root.left
                sub_root.left = None

            # At this point, the tree restructuring at the current subtree is done.
            # Right now, from original sub_root.right's point of view, last_node is
            # in the original sub_root's position. So if last_node.right is not a
            # nullptr, we recurse right.
            if last_node.right is not None:
                last_node = do_flattening(last_node.right)

            # Return the last node in the current subtree.
            return last_node

        # We only need to do_flattening on root if the root node is not a nullptr.
        if root is not None:
            do_flattening(root)

        return None


r = TreeNode(1)
r.left = TreeNode(2)
r.left.left = TreeNode(3)
r.left.right = TreeNode(4)
r.right = TreeNode(5)
r.right.right = TreeNode(6)
Solution().flatten(r)
print()
