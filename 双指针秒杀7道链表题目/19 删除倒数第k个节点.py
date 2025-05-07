# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-1)
        dummy.next=head
        p1=dummy
        p2=dummy
        if not head:
            return []
        for i in range(n+1):
            p1=p1.next
        while p1:
            p1=p1.next
            p2=p2.next
        p2.next=p2.next.next
        return dummy.next

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

solution=Solution()
ans=solution.removeNthFromEnd(head,2)
while ans:
    print(ans.val)
    ans=ans.next