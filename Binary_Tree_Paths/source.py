# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def binaryTreePaths(self, root: TreeNode):

        # Strategy:
        # Do preorder traversal through the tree until we reach a (none None) leaf node
        # As we traverse from the root to the leaf, we keep track of traversed tree nodes
        # Once we get to the leaf, we generate a root-to-leaf string and append it
        # to our return list containing binary tree paths.
        # As we traverse back towards the root (in order to explore different branches of the tree),
        # we remove our current node from the current_path list.
        # We keep on traversing through the tree until we reached all the leaves in the tree

        # The current root-to-current node path
        current_path = []

        # The final return list of binary tree paths
        tree_paths = []

        # Get the final return list of binary tree paths by traversing through the tree
        # in pre-order traversal
        self.get_tree_paths_preorder_traversal(root, current_path, tree_paths)

        return tree_paths

    def get_tree_paths_preorder_traversal(self, root, current_path, tree_paths):

        # We traverse deeper if the current root node is not nullptr
        if root is not None:

            # Append the current root node to the current_path list
            current_path.append(root)

            # If we reached a (none None) leaf node, we generate the root to leaf node path string
            # Then add the path string to tree_paths list
            if root.left is None and root.right is None:
                path_string = self.get_current_path_string(current_path)
                tree_paths.append(path_string)

            # Otherwise, we keep traversing through the tree
            else:
                self.get_tree_paths_preorder_traversal(root.left, current_path, tree_paths)
                self.get_tree_paths_preorder_traversal(root.right, current_path, tree_paths)

            # At this point, we are finished doing whatever we needed to do with this current root node
            # So we remove it from our current_path
            current_path.pop(-1)

        return

    def get_current_path_string(self, current_path) -> str:

        # Generate root to (none None) leaf node path string

        path_string = str(current_path[0].val)
        for node in current_path[1:]:
            path_string += '->' + str(node.val)

        return path_string


r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.right = TreeNode(5)

lst = Solution().binaryTreePaths(r)

print()
