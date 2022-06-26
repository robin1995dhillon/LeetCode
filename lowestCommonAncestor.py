class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def commonAncestor(root, p, q):
    if root is None:
        return None
    if root.val == p.val or root.val == q.val:
        return root

    left_node = commonAncestor(root.left, p, q)
    right_node = commonAncestor(root.right,p,q)

    if(left_node is None and right_node is None):
        return None
    elif(left_node is not None and right_node is not None):
        return root

    if(left_node is None):
        return right_node
    return left_node
