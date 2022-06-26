class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution(object):
    def levelOrder(self, root):
        ans = []
        if root is None:
            return ans
        queue = []

        queue.append(root)
        while (queue):
            temp = []
            n = len(queue)
            for i in range(0,n):
                top_val = queue.pop(0)
                print("top val is :",top_val.val)
                temp.append(top_val.val)
                if top_val.left is not None:
                    queue.append(top_val.left)
                if top_val.right is not None:
                    queue.append(top_val.right)
            if(len(temp)>0):
                ans.append(temp[:])  # When reading, list is a reference to the original list, and list[:] shallow-copies the list.

# When assigning, list (re)binds the name and list[:] slice-assigns, replacing what was previously in the list.
#
# Also, don't use list as a name since it shadows the built-in.

                temp.clear()
        return ans

root = Node(3)
root.left = Node(9)
# root.left.left = Node(3)
# root.left.right = Node(5)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
sol = Solution()
value = sol.levelOrder(root)
print(value)