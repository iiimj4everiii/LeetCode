# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes(self, root) -> int:

        # A function to get the max tree height. The leftmost node in
        # a complete binary tree is guarantee to have the max height.
        def get_max_height(curr):

            depth = 0
            while curr.left is not None:
                curr = curr.left
                depth += 1

            return depth

        # Check if the node after traversing path is a nullptr.
        def is_leaf_None(curr, path):

            for direction in path:
                if direction == '0':
                    curr = curr.left
                else:
                    curr = curr.right

            if curr is None:
                return True

            return False

        # Corner case 1: If root is nullptr, return 0.
        if root is None:
            return 0

        # Get the max height of the tree.
        max_height = get_max_height(root)

        # Corner case: If the max height is 0, then we only have root
        # node in our tree. Simply return 1.
        if max_height is 0:
            return 1

        # Since we know our tree is a complete tree, we can calculate
        # the number of non-leaf nodes.
        non_leaf_level_node_count = 2 ** max_height - 1

        # FIRST MAJOR INSIGHT:
        # In order to get better than O(n) time complexity, we will use
        # binary search method on the leaf nodes to find the transition
        # point between a leaf node at max height and a leaf node at
        # max height - 1. Since it takes log(n) to traverse from root to
        # leaf and log(n) to do binary search, the time complexity for
        # our algorithm will be O(log(n)*log(n)) = O(log(n)).

        # If h is the max height of the tree, then we can have up to
        # 2^h leaf nodes in this tree. Therefore, we will initialize the
        # left index (l_idx) to 0 and the right index (r_idx) to 2^h - 1.
        l_idx = 0
        r_idx = 2 ** max_height - 1

        # Binary search termination condition: r_idx >= l_idx
        while l_idx < r_idx:

            # Get the mid index m_idx
            m_idx = (l_idx + r_idx) // 2

            # SECOND MAJOR INSIGHT:
            # It looks like there is a correlation between root-to-
            # (m)th-leaf traversal path and the binary representation
            # of m. For example, if we want to go from root to the 9th
            # leaf node on the 4th level, we go Right->Left->Left->Right.
            # The binary representation of 9 = (1001) correlation to
            # (RLLR). I am not sure how this happens but it seems to be
            # the case.

            # Get the direction on how to travel from root to the
            # (m_idx)th leaf position.
            traversal_path = format(m_idx, '0' + str(max_height) + 'b')

            # If the (m_idx)th leaf node is None, we set right = mid.
            if is_leaf_None(root, traversal_path):
                r_idx = m_idx

            # Otherwise, we set left = mid + 1.
            else:
                l_idx = m_idx + 1

        # At this point, l_idx == r_idx. We are also at the transition
        # point. So we know that we have at least l_idx number of leaf-
        # level node count.
        leaf_level_node_count = l_idx

        # All we have to do now is to check if the node at index l_idx
        # leaf-level leaf node position is non-nullptr. If it is non-
        # nullptr, we add to leaf_level_node_count.
        traversal_path = format(l_idx, '0' + str(max_height) + 'b')
        if not is_leaf_None(root, traversal_path):
            leaf_level_node_count += 1

        # Return the sum of non-leaf-level node count and leaf-level
        # node count.
        return non_leaf_level_node_count + leaf_level_node_count


r = TreeNode(1)

r.left = TreeNode(2)
r.right = TreeNode(3)

r.left.left = TreeNode(4)
r.left.right = TreeNode(5)
r.right.left = TreeNode(6)
r.right.right = TreeNode(7)

r.left.left.left = TreeNode(8)
r.left.left.right = TreeNode(9)
r.left.right.left = TreeNode(10)
r.left.right.right = TreeNode(11)
# r.right.left.left = TreeNode(12)
# r.right.left.right = TreeNode(13)
# r.right.right.left = TreeNode(14)
# r.right.right.right = TreeNode(15)

sol = Solution().countNodes(r)
print(sol)
