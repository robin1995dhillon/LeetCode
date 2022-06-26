class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, target_val):
        if head is None:
            return
        temp = ListNode(0)
        temp.next = head
        head = temp
        while temp is not None and temp.next is not None:
            if temp.next.val != target_val:
                temp = temp.next
            else:
                target_node = temp.next
                temp.next = target_node.next
                target_node.next = None
        return head.next


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(6)
node_4 = ListNode(3)
node_5 = ListNode(4)
node_6 = ListNode(5)
node_7 = ListNode(6)

# node_1 = ListNode(7)
# node_2 = ListNode(7)
# node_3 = ListNode(7)
# node_4 = ListNode(7)
# node_5 = ListNode(7)
# node_6 = ListNode(7)
# node_7 = ListNode(7)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6
node_6.next = node_7

# head = [1,2,6,3,4,5,6]
val = 6
sol = Solution()
ans = sol.removeElements(node_1, val)
while ans is not None:
    print(ans.val)
    ans = ans.next
