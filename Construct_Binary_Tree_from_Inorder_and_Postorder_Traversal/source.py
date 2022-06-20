# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):

        # Problem:
        # Given two integer arrays inorder and postorder where inorder is the inorder traversal
        # of a binary tree and postorder is the postorder traversal of the same tree, construct
        # and return the binary tree.

        # Strategy:
        # We will use a very similar strategy as in the previous problem:
        # Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal
        # We will build the entire binary tree by building by recursively build its left subtree
        # and its right subtree.

        # The most important thing to notice is that the root node (and
        # the sub-roots) divides (and subdivides) the inorder traversal list into 2 subtrees:
        # 1) From the beginning of list up to but not including the root.
        # 2) From the end of the list down to but not including the root.

        # This behavior is the same in the subtrees where the sub-root divides the inorder
        # sub-list into 2 more regions from the beginning of the sub-list up to but not including
        # the sub-root and from the end of the sub-list down to but not including the sub-root.
        # So on and so forth.

        # The second important thing to notice is that the nodes/node values in THE INVERTED
        # POSTORDER list tells us the most recent node value but prioritizing the right node
        # instead of the left node. In this case, it tells us the value of the root/
        # sub-root. We use this value to find the index into the inorder list to help us divide/
        # subdivide the inorder list/sub-lists.
        # When we get to the point where we can no longer subdivide the inorder sub-list, we
        # return nullptr (leaf) node to its parent.

        def build(postorder, inorder, l_start, r_stop, next_po_idx, inorder_idx):

            # Termination condition: if the left start index is greater than the right stop index.
            # Simply return a nullptr node and the unchanged next_po_idx.
            if l_start > r_stop:
                return None, next_po_idx

            # The (next_po_idx)th position in postorder list holds the new node's value to be
            # processed. Create a new TreeNode with the value at the (next_po_idx)th position in
            # postorder list and this will be our sub-root.
            root = TreeNode(postorder[next_po_idx])

            # Increment next_po_idx to the next index.
            next_po_idx += 1

            # We subdivide the inorder list into 2 additional regions:
            # 1) [l_start, l_stop]
            # 2) [r_start, r_stop]
            # where index of the new node's value in inorder list is between l_stop and r_start.
            # Recursive build the left subtree with values in the inorder list from index l_start
            # to l_stop. Likewise, recursively build the right subtree with values in the inorder
            # list from r_start to r_stop.

            # Since the inverted postorder traversal prioritizes right node first, we will go
            # right then left, instead of left then right.
            r_start = inorder_idx[root.val] + 1
            root.right, next_po_idx = build(postorder, inorder, r_start, r_stop, next_po_idx, inorder_idx)

            l_stop = inorder_idx[root.val] - 1
            root.left, next_po_idx = build(postorder, inorder, l_start, l_stop, next_po_idx, inorder_idx)

            # At this point, we have a subtree rooted at root. We also have the updated next_po_idx.
            # Return both of these to the parent node.
            return root, next_po_idx

        # Create a dictionary of inorder list values to their index lookup.
        inorder_idx = {}
        for i in range(len(inorder)):
            inorder_idx[inorder[i]] = i

        # Call the build function to recursively build the binary tree. We will pass the inverted
        # postorder list here, rather than direct pass.
        solution, _ = build(postorder[::-1], inorder, 0, len(inorder) - 1, 0, inorder_idx)

        return solution


post_order = [9,15,7,20,3]
in_order = [9,3,15,20,7]
sol = Solution().buildTree(in_order, post_order)
print()


