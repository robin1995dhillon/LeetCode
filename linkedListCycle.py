class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        hare = head
        turtle  = head
        while(hare and turtle and hare.next):
            hare = hare.next.next
            turtle = turtle.next
            if hare == turtle:
                return True
        return False

sol = Solution()
node_1 = ListNode(1)
node_5 = ListNode(5)
node_11 = ListNode(11)
node_8 = ListNode(8)
node_9 = ListNode(9)

node_1.next = node_5
node_5.next = node_11
node_11.next = node_8
node_8.next = node_9
node_9.next = node_5

answer = sol.hasCycle(node_1)
print(answer)