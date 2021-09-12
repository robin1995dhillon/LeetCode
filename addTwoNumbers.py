class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = ListNode()
        pointer = ans
        carry = 0
        summation = 0
        while (l1 or l2):
            summation = carry
            if (l1):
                summation += l1.val
                l1 = l1.next
            if (l2):
                summation += l2.val
                l2 = l2.next
            carry = int(summation / 10)
            pointer.next = ListNode(summation % 10)
            pointer = pointer.next
        if(carry > 0):
            pointer.next = ListNode(carry)
        return ans.next


sol = Solution()

l1_2 = ListNode(2)
l1_4 = ListNode(4)
l1_3 = ListNode(3)

l1_2.next = l1_4
l1_4.next = l1_3


l2_5 = ListNode(5)
l2_6 = ListNode(6)
l2_4 = ListNode(4)

l2_5.next = l2_6
l2_6.next = l2_4

value = sol.addTwoNumbers(l1_2,l2_5)
while (value is not None):
    print(value.val)
    value = value.next