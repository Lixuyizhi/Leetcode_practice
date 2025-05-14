
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self):
        successor=None
    def reverseList(self, head,n):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if n==1:
            self.successor = head.next
            return head


        last =self.reverseList(head.next, n-1)
        head.next.next = head
        head.next=self.successor
        return last






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