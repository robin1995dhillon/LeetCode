class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def maxDepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1



root = Node(8)
root.left = Node(4)
root.left.left = Node(3)
root.left.right = Node(5)
root.right = Node(9)
val = maxDepth(root)
print(val)