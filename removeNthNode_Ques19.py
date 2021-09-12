class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        ans = ListNode
        ans.next = head
        first = ans
        second = ans
        for i in range(1,n+2):
            first = first.next

        while(first is not None):
            first = first.next
            second = second.next
        second.next = second.next.next

        return ans.next

sol = Solution()

node_1 = ListNode(1)
node_3 = ListNode(3)
node_5 = ListNode(5)
node_7 = ListNode(7)

node_1.next = node_3
node_3.next = node_5
node_5.next = node_7

answer = sol.removeNthFromEnd(node_1,2)

while (answer is not None):
    print(answer.val)
    answer = answer.next