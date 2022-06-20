# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode):

        # Handling special cases:
        if root is None:
            return True

        # Create a left subtree stack and a right subtree stack
        left_subtree_queue = [root.left]
        right_subtree_queue = [root.right]

        while len(left_subtree_queue) > 0 and len(right_subtree_queue) > 0:

            # Level-order traversal: pop the front element
            left_node = left_subtree_queue.pop(0)
            right_node = right_subtree_queue.pop(0)

            # If left node is None
            if left_node is None:

                # Return false if right node is NOT none
                if right_node is not None:
                    return False
                # Keep going if right node is none
                else:
                    continue

            # If right node is None
            if right_node is None:

                # Return false if left node is NOT none
                if left_node is not None:
                    return False
                # Keep going if left node is none
                else:
                    continue

            # At this point, both left and right nodes are NOT none
            if not left_node.val == right_node.val:
                return False
            else:
                # Queuing their children
                left_subtree_queue.append(left_node.left)
                left_subtree_queue.append(left_node.right)
                right_subtree_queue.append(right_node.right)
                right_subtree_queue.append(right_node.left)

        if len(left_subtree_queue) == 0 and len(right_subtree_queue) == 0:
            return True

        return False


if __name__ == "__main__":
    root = TreeNode(1)

    # root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    #
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(3)

    print(Solution().isSymmetric(None))
