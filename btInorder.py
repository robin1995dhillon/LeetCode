class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)


s = Solution()
root = Node(1)
root.left = None
root.right = Node(2)
root.right.left = Node(3)
root.right.right = None
ans = s.inorderTraversal(root)
print(ans)
