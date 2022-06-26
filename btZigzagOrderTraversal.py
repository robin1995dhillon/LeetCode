from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def zigzag(self, root):
        queue = deque([root])
        ans = []
        if root is None:
            return ans
        count = False
        while (queue):
            queue_length = len(queue)
            temp_list = []

            for node_val in range(0, queue_length):
                if not count:
                    popped_node = queue.popleft()
                if count:
                    popped_node = queue.pop()

                temp_list.append(popped_node.val)
                if not count:
                    if popped_node.left is not None:
                        queue.append(popped_node.left)
                        print(popped_node.left.val)

                    if popped_node.right is not None:
                        queue.append(popped_node.right)
                        print(popped_node.right.val)

                if count:
                    if popped_node.right is not None:
                        queue.appendleft(popped_node.right)
                    if popped_node.left is not None:
                        queue.appendleft(popped_node.left)




                    # continue
                # else:
                #     popped_node = queue.popleft()
                #     temp_list.append(popped_node.val)

                    # count = not count
                    # continue
            ans.append(temp_list[:])
            temp_list.clear()
            count = not count
        print(ans)


# root = Node(0)
# root.left = Node(2)
# root.right = Node(4)
# root.left.left = Node(1)
# root.left.left.left = Node(5)
# root.left.left.right = Node(1)
# root.right.left = Node(3)
# root.right.left.right = Node(6)
#
# root.right.right = Node(-1)
# root.right.right.right = Node(8)

# [[0],[4,2],[1,3,-1],[8,6,1,5]]

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# root = Node(3)
# root.left = Node(9)
# root.right = Node(20)
# root.right.left = Node(15)
# root.right.right = Node(7)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

root.zigzag(root)