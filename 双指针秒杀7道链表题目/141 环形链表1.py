# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1=head
        p2=head
        while p1 and p1.next :
            p1=p1.next.next
            p2=p2.next
            if p1 == p2:
              return True
        return False

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=head.next.next

solution=Solution()
print(solution.hasCycle(head))
