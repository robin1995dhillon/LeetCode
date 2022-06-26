class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = None


# def delete(root, key):
#     if root is None:
#         return "No node present"
#     if (root.data == key):
#         if (root.left is None and root.right is None):
#             root = None
#             print("node deleted")
#         elif()
#     if (root.data > key):
#         delete(root.left, key)



root = Node(8)
root.left = Node(4)
root.left.left = Node(3)
root.left.right = Node(5)
root.right = Node(9)
