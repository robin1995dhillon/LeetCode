class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def inorder(root):
    if (root is not None):
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def preorder(root):
    if (root is not None):
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if (root is not None):
        postorder(root.left)
        postorder(root.right)
        print(root.val)


root = Node(5)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(8)
# inorder(root)
# preorder(root)
postorder(root)
