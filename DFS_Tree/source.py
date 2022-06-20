class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, res) -> list:

    if root is None:
        return res

    if root.left is not None:
        res = dfs(root.left, res)

    if root.right is not None:
        res = dfs(root.right, res)

    res.append(root.val)

    return res


root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(6)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

res = dfs(root, [])
print(res)
