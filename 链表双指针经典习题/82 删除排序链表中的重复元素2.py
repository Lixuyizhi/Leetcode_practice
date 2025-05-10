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
        dummyUniq = ListNode(-101)
        dummyDup = ListNode(-101)
        puniq, pdup = dummyUniq, dummyDup
        p = head

        while p:
            if (p.next is not None and p.val == p.next.val) or p.val == pdup.val:
                pdup.next = p
                pdup = pdup.next
            else:
                puniq.next = p
                puniq = puniq.next
            temp = p.next
            p.next = None
            p = temp
        return dummyUniq.next

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