# Time = O(N)
# Space = O(1)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        cur = ListNode(0)
        ans = cur
        while (l1 and l2):
            if (l1.val > l2.val):
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        while (l1):
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while (l2):
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return ans.next


l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_4 = ListNode(4)

l1_1.next = l1_2
l1_2.next = l1_4


l2_1 = ListNode(1)
l2_3 = ListNode(3)
l2_4 = ListNode(4)

l2_1.next = l2_3
l2_3.next = l2_4

sol = Solution()
value = sol.mergeTwoLists(l1_1, l2_1)

while(value is not None):
    print(value.val)
    value = value.next