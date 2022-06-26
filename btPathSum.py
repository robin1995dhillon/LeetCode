class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def hasSum(root, sum,cur):
    if root is None:
        return False
    cur += root.val
    if(cur==sum and root.left is None and root.right is None):
        return True
    return (hasSum(root.right,sum,cur) or hasSum(root.left,sum,cur))


def hasPathSum(root,sum):
    return hasSum(root,sum,0)
root = Node(8)
root.left = Node(4)
root.left.left = Node(3)
root.left.right = Node(5)
root.right = Node(9)
val = hasPathSum(root, 15)
print(val)
