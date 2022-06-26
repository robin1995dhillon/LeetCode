class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [True,0]
            left,right = dfs(root.left),dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1+max(left[1],right[1])]
        return dfs(root)[0]



s = Solution()
root = Node(1)
root.left = Node(3)
root.right = Node(20)
root.right.right = Node(7)
root.right.left = Node(15)
ans = s.isBalanced(root)
print(ans)