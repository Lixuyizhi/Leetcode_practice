# Definition for singly-linked list.
from scipy.linalg import solve_lyapunov


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head,n):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        pre,cur,nex=None,head,head.next

        while n>0:
            cur.next=pre
            pre=cur
            cur=nex
            if nex:
                nex=nex.next
            n-=1
        head.next=cur
        return pre
listnode=ListNode(1)
listnode.next=ListNode(2)
listnode.next.next=ListNode(3)
listnode.next.next.next=ListNode(4)
listnode.next.next.next.next=ListNode(5)
listnode.next.next.next.next.next=ListNode(6)
listnode.next.next.next.next.next.next=ListNode(7)

solution = Solution()
newhead = solution.reverseList(listnode,3)
while newhead:
    print(newhead.val)
    newhead = newhead.next