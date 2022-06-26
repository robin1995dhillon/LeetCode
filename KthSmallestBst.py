class Node:
    def __init__(self, val):

        self.left = None
        self.right = None
        self.val = val

    def kthSmallest(self,root1, k):
        self.res = None
        self.k = k
        self.inorder(root1)
        return self.res

    def inorder(self,roots):
        if not roots:
            return
        self.inorder(roots.left)
        self.k -= 1
        print(self.k)
        if self.k == 0:
            self.res = roots.val
            return self.res
        self.inorder(roots.right)





root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(1)
val = root.kthSmallest(root, 3)
print(val)
