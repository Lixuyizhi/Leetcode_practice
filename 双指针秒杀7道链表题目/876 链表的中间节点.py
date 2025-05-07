# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1=head
        p2=head
        while p1!=None and p1.next!=None:
            p1=p1.next.next
            p2=p2.next
        return p2

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

solution = Solution()
ans=solution.middleNode(head)
print(ans.val)
