# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def lowestCommonAncestor(self, root, p, q):

        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # There are only 3 cases:
        # 1) If both p and q are greater than parent, search the right subtree
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # 2) If both p and q are lesser than parent, search the right subtree
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # 3) We have found the split point, i.e. the LCA node.
        else:
            return root

    # p_ancestors = set()
    # q_ancestors_stack = []
    # is_p = True
    #
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #
    #     # Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
    #     # According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes
    #     # p and q as the lowest node in T that has both
    #     # p and q as descendants (where we allow a node to be a descendant of itself).”
    #
    #     # This problem is fairly complex
    #     # Strategy:
    #     # Find all the ancestors of p including p itself and store them in a set
    #     # Find all the ancestors of q including q itself and store them in a stack/list
    #     # Iterate q's ancestors backward until we find an ancestor that is in ancestor p's set
    #
    #     self.is_p = True
    #     # The arguments look complicated because we are passing a function pointer: self.p_ancestors.add
    #     # Passing a function pointer allow us to reuse get_ancestors method
    #     self.get_ancestors(root, p, add_item_fn=self.p_ancestors.add)
    #
    #     self.is_p = False
    #     # The arguments look complicated because we are passing a function pointer: self.q_ancestors_stack.append
    #     self.get_ancestors(root, q, add_item_fn=self.q_ancestors_stack.append)
    #
    #     # Look through the q's ancestor stack from closest to furthest to find the closest common ancestor
    #     for lowest_common_ancestor in reversed(self.q_ancestors_stack):
    #         # Check to see if we can find a common ancestor in p's ancestor
    #         if lowest_common_ancestor in self.p_ancestors:
    #             return lowest_common_ancestor
    #
    #     return None
    #
    # def get_ancestors(self, curr_node, target_node, add_item_fn) -> bool:
    #
    #     # If we reached a leaf node, then we did not find the target node in this subtree
    #     if curr_node is None:
    #         return False
    #
    #     # Add the current node to the ancestor list (this node will be removed
    #     # if we cannot find the target node in this subtree rooted at curr_node)
    #     add_item_fn(curr_node)
    #
    #     # If we found the target node, we return True
    #     if curr_node == target_node:
    #         return True
    #
    #     # Otherwise, explore the left subtree
    #     target_found = self.get_ancestors(curr_node.left, target_node, add_item_fn)
    #     # and the right subtree
    #     target_found = target_found or self.get_ancestors(curr_node.right, target_node, add_item_fn)
    #
    #     # If we did not find the target node in the left subtree, the right subtree,
    #     # and in the curr_node (current root node), then we know that curr_node
    #     # is not target node's ancestor. Curr_node should be removed from the ancestor's set/list
    #     if not target_found:
    #         if self.is_p:
    #             self.p_ancestors.remove(curr_node)
    #         else:
    #             self.q_ancestors_stack.pop(-1)
    #
    #     return target_found


r = TreeNode(6)
r.left = TreeNode(2)
r.right = TreeNode(8)

r.left.left = TreeNode(0)
r.left.right = TreeNode(4)
r.right.left = TreeNode(7)
r.right.right = TreeNode(9)

r.left.right.left = TreeNode(3)
r.left.right.right = TreeNode(5)

# r = TreeNode(3)
# r.left = TreeNode(1)
# r.right = TreeNode(4)
#
# r.left.right = TreeNode(2)

p0 = r.left.right.left
q0 = r.right.right
t = Solution().lowestCommonAncestor(r, p0, q0)

print()
