# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):

        # Get the ancestors of p.
        p_ancestors = []
        self.get_ancestors(root, p, p_ancestors)

        # Get the ancestors of q.
        q_ancestors = []
        self.get_ancestors(root, q, q_ancestors)

        # W.L.O.G., we create a set of p's ancestors. Then walk
        # through the ancestors of q, starting from q itself
        # until we reach a common ancestor with p (exists in p's
        # ancestor set) or the root.
        p_ancestors_set = set(p_ancestors)
        for ancestor in q_ancestors:
            if ancestor in p_ancestors_set:
                return ancestor

        return root

    # Use post-order traversal to get the ancestors of descendant.
    # This method returns ancestors in order from NEWEST TO OLDEST.
    # This method returns True if descendant is found in the tree.
    # Once descendant is found, we can START RECORDING the ancestors
    # as we travel back up the tree.
    def get_ancestors(self, root, descendant, ancestors):

        if root is None:
            return False

        if self.get_ancestors(root.left, descendant, ancestors):
            ancestors.append(root)
            return True

        if self.get_ancestors(root.right, descendant, ancestors):
            ancestors.append(root)
            return True

        if root is descendant:
            ancestors.append(root)
            return True

        return False

    # Use pre-order traversal to get the ancestors of descendant.
    # This method returns ancestors in order from OLDEST TO NEWEST.
    # This method returns True if descendant is found in the tree.
    # Once descendant is found, we STOP REMOVING nodes and unwind
    # back to the root.
    def get_ancestors2(self, root, descendant, ancestors):

        if root is None:
            return False

        ancestors.append(root)
        if root is descendant:
            return True

        if self.get_ancestors2(root.left, descendant, ancestors):
            return True

        if self.get_ancestors2(root.right, descendant, ancestors):
            return True

        ancestors.pop(-1)

        return False


r = TreeNode(3)

r.left = TreeNode(5)
r.right = TreeNode(1)

r.left.left = TreeNode(6)
r.left.right = TreeNode(2)

r.right.left = TreeNode(0)
r.right.right = TreeNode(8)

r.left.right.left = TreeNode(7)
r.left.right.right = TreeNode(4)

sol = Solution().lowestCommonAncestor(r, r.left, r.left.right.right)
print(sol.val)
