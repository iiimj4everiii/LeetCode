# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDepth(self, root: TreeNode) -> int:

        # Handling the corner cases
        if root is None:
            return 0

        # Using queue to traverse the binary tree row by row
        # Once we find a None node, then we have reached the minimum depth
        queue = [root]
        depth = 1
        while len(queue) > 0:

            # INSIGHT:
            # queue will only contain the current generation and their children
            # No grandchildren are in the queue at anytime.
            n = len(queue)

            for i in range(n):

                # Pop the front element
                current_node = queue.pop(0)

                # Process the front element
                if current_node is not None:

                    # If the current_node has no children,
                    # then the depth of this node is the minimum depth of the binary tree
                    if current_node.left is None and current_node.right is None:
                        return depth

                    # Push the children of the front element to the back.
                    queue.append(current_node.left)
                    queue.append(current_node.right)

            depth += 1

        return depth


root = TreeNode(2)

root.right = TreeNode(3)

root.right.right = TreeNode(4)

root.right.right.right = TreeNode(5)

root.right.right.right.right = TreeNode(6)

print(Solution().minDepth(root))
