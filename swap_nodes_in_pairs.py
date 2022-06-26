# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        temp = ListNode(0)
        temp.next = head
        head = temp
        temp2 = head.next

        print(head.val)
        print(temp2.val)
        q = temp
        print(q.val)
        p = temp2.next
        print(p.val)
        while temp2.next is not None:
            q.next = p
            temp2.next = p.next
            p.next = temp2
            q = temp2
            print("value of q is----------"+str(q.val))
            if(temp2.next is not None):
                temp2 = temp2.next
                p = temp2.next

        value_list  = self.print_list(head)
        return value_list

    def print_list(self, head):
        temp = head.next
        print("temp val is-------------"+str(temp.val))
        linkedList = []
        while (temp):
            linkedList.append(temp.val)
            temp = temp.next
        return linkedList


linked_list = Solution()

second_node = ListNode(1)
third_node = ListNode(2)
fourth_node = ListNode(3)
# fifth_node = ListNode(4)

second_node.next = third_node
third_node.next = fourth_node
# fourth_node.next = fifth_node

value = linked_list.swapPairs(second_node)
print(value)
