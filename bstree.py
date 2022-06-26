class Node:
    def __init__(self,val):
        self.left=None
        self.right = None
        self.val = val
def insert(root,node):
    if(root is None):
        root = node
        return root
    elif(node.val<root.val):
        if(root.left is None):
            root.left = node
        else:
            insert(root.left,node)
    else:
        if(node.val>root.val):
            if(root.right is None):
                root.right = node
            else:
                insert(root.right,node)
def preorder(root):
    if(root is not None):
        print(root.val)
        preorder(root.left)
        preorder(root.right)

root = Node(5)
insert(root,Node(6))
insert(root,Node(4))
insert(root,Node(9))
insert(root,Node(7))
insert(root,Node(1))


preorder(root)