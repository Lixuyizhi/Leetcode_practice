# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-101)
        p1=dummy
        p2=head

        while p2:
            if p2.val != p1.val:
                p1.next=p2
                p1=p1.next
            temp=p2.next
            p2.next=None
            p2=temp
        return dummy.next


exap=ListNode(1)
exap.next=ListNode(2)
exap.next.next=ListNode(2)
exap.next.next.next=ListNode(3)
exap.next.next.next.next=ListNode(3)
exap.next.next.next.next.next=ListNode(5)

solution = Solution()
ans=solution.deleteDuplicates(exap)
while ans:
    print(ans.val)
    ans=ans.next