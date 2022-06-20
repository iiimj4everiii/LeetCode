# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    # Strategy:
    # Typically, we will use recursion to traverse the entire
    # tree in an in-order faction. We rely on the recursive
    # stack in that case. However in this problem, we may not
    # traverse the entire tree and therefore cannot rely on
    # recursion to do this problem. Instead, we will keep a
    # stack of ancestors that we have visited along the way to
    # a leaf node. For constructor, we append root to our
    # ancestor stack and traverse all the way to the leftmost
    # leaf node, appending ancestors to the stack.

    # For next() method, we pop off from the ancestor stack,
    # take its value, then traverse to the leftmost leaf node
    # in the right subtree. This way, we always start at the
    # leftmost leaf node of a subtree.

    # For hasNext(), we return True if there are ancestors
    # in the stack

    def __init__(self, root):
        # For constructor, we append root to our ancestor
        # stack and traverse all the way to the leftmost leaf
        # node, appending ancestors to the stack.
        self.ancestors = [root]

        current_node = root
        while current_node.left is not None:
            current_node = current_node.left
            self.ancestors.append(current_node)

    def next(self) -> int:

        # For next() method, we pop off from the ancestor stack,
        # take its value, then traverse to the leftmost leaf node
        # in the right subtree. This way, we always start at the
        # leftmost leaf node of a subtree.

        current_node = self.ancestors.pop(-1)

        result = current_node.val

        if current_node.right is not None:
            current_node = current_node.right
            self.ancestors.append(current_node)
            while current_node.left is not None:
                current_node = current_node.left
                self.ancestors.append(current_node)

        return result

    def hasNext(self) -> bool:

        # For hasNext(), we return True if there are ancestors
        # in the stack

        return len(self.ancestors) > 0


# Your BSTIterator object will be instantiated and called as such:
root = TreeNode(7)

root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)

root.left.right.left = TreeNode(4)

root.left.right.left.left = TreeNode(3)
root.left.right.left.right = TreeNode(5)

obj = BSTIterator(root)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
