# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

listnode=ListNode(1)
listnode.next=ListNode(2)
listnode.next.next=ListNode(3)
listnode.next.next.next=ListNode(4)
listnode.next.next.next.next=ListNode(5)
listnode.next.next.next.next.next=ListNode(6)
listnode.next.next.next.next.next.next=ListNode(7)

solution = Solution()
newhead = solution.reverseList(listnode)
while newhead:
    print(newhead.val)
    newhead = newhead.next
