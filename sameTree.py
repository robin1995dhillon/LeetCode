class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        p_val = self.preorder(p)
        q_val = self.preorder(q)
        print(p_val)
        print(q_val)
        if p_val == q_val:
            return True
        else:
            return False

    def preorder(self,root):
        if root is None:
            return ["null"]
        return [root.val]+self.preorder(root.left)+self.preorder(root.right)


s = Solution()

root = Node(1)
root.left = Node(1)
root.right = None

root2 = Node(1)
root2.left = None
root2.right = Node(1)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
#
# root2 = Node(1)
# root2.left = Node(2)
# root2.right = Node(3)
ans = s.isSameTree(root,root2)
print(ans)