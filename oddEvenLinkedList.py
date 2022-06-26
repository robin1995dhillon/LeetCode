
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        if(not head):
            return head
        odd = head
        even = odd.next
        evenList = even

        while(even and even.next):
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenList
        return head

sol = Solution()

node_10 = ListNode(10) #1
node_20 = ListNode(20) #2
node_30 = ListNode(30) #3
node_40 = ListNode(40) #4
node_50 = ListNode(50) #5

node_10.next = node_20
node_20.next = node_30
node_30.next = node_40
node_40.next = node_50

value = sol.oddEvenList(node_10)

while(value is not None):
    print(value.val)
    value = value.next
