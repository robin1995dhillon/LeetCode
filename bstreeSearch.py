class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def search(root, key):
    if root is None:
        print("node not found...")
    elif (root.val == key):
        print("node found")
    elif (root.val > key):
        search(root.left, key)
    elif (root.val < key):
        search(root.right, key)



root = Node(8)
root.left = Node(4)
root.left.left = Node(3)
root.left.right = Node(5)
root.right = Node(9)
search(root, 1)
