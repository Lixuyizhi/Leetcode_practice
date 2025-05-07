# Definition for singly-linked list.
from scipy.linalg import solve


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            temp = p.next
            p.next = None
            p = temp
        p1.next = dummy2.next
        return dummy1.next

node=ListNode(1)
node.next=ListNode(4)
node.next.next=ListNode(3)
node.next.next.next=ListNode(2)
node.next.next.next.next=ListNode(5)
node.next.next.next.next.next=ListNode(2)
x=3

solution = Solution()
head = solution.partition(node, x)
while head:
    print(head.val)
    head = head.next


