# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Strategy:
        # Since we are dealing with a Binary Search Tree, the nodes should be sorted
        # if we traverse the tree in-order. Since there will only be 2 misplaced nodes
        # in the tree, there can only be 2 cases:
        # 1) The 2 misplaced nodes are directly next to each other in an in-order
        #    traversal.
        # 2) The 2 misplaced nodes are separated by another node in an in-order
        #    traversal.
        # We will traverse the tree in-order and find the first node that is smaller
        # than the previous node. The previous node must be the first misplaced node,
        # ptr1. Since there are only 2 cases of misplaced nodes, we assume that the
        # second misplaced node, ptr2, is the current node. Then we continue to traverse
        # through the tree in-order and try to find the second occurrence of the current
        # node being smaller than its previous node. If we find this second occurrence,
        # ptr2 node must be the current node and we are looking at case 2 scenario.
        # Return both misplaced nodes: ptr1 and ptr2. Then swap the value between these
        # two nodes.

        def in_order_traversal(node, prev_node, ptr1, ptr2):

            # Termination condition: if node is None, just return the parameters.
            if node is None:
                return prev_node, ptr1, ptr2

            # In-order traversal step 1: go left first.
            prev_node, ptr1, ptr2 = in_order_traversal(node.left, prev_node, ptr1, ptr2)

            # In-order traversal step 2: do something.
            if prev_node is not None:
                # Notice that there are only 2 cases here:
                # 1) The two nodes are right next to each other.
                # 2) The two nodes are separated by another node.
                if node.val <= prev_node.val:
                    # Assume that we are dealing with case 1.
                    if ptr1 is None:
                        ptr1 = prev_node
                        ptr2 = node
                    # If it turns out to be case 2, then we update ptr2.
                    else:
                        ptr2 = node
                        return prev_node, ptr1, ptr2

            # Assign to prev_node our current node.
            prev_node = node

            # In-order traversal step 3: go right last.
            prev_node, ptr1, ptr2 = in_order_traversal(node.right, prev_node, ptr1, ptr2)

            # Return whatever we find after going right.
            return prev_node, ptr1, ptr2

        # Initialize ptr1 and ptr2 to None. These will point to the two nodes that are
        # misplaced.
        ptr1 = None
        ptr2 = None
        _, ptr1, ptr2 = in_order_traversal(root, None, ptr1, ptr2)

        # Swap the values between the two misplaced nodes.
        ptr1.val, ptr2.val = ptr2.val, ptr1.val

        return


# r = TreeNode(3)
# r.left = TreeNode(1)
# r.right = TreeNode(4)
# r.right.left = TreeNode(2)
# r = TreeNode(1)
# r.left = TreeNode(3)
# r.left.right = TreeNode(2)
r = TreeNode(3)
r.left = TreeNode(5)
Solution().recoverTree(r)
print()
