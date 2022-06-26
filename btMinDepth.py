class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0

        self.small = float('inf')

        def dfs(root, num):
            if root is None:
                return
            if root.left is None and root.right is None:
                self.small = min(self.small,num)
            dfs(root.left,num+1)
            dfs(root.right, num + 1)
        dfs(root,1)
        return self.small

s = Solution()
# root = Node(3)
# root.left = Node(9)
# root.right.left = Node(3)
# root.right.right = Node(5)
# root.right = Node(20)

root = Node(2)
root.right = Node(3)
root.right.right = Node(4)
root.right.right.right = Node(5)
root.right.right.right.right = Node(6)

value = s.minDepth(root)
print(value)
