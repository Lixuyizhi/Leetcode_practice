# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == 1:
            return reverseNnode(head, right)
        pre = head
        for i in range(1, left - 1):
            pre = pre.next
        pre.next = reverseNnode(pre.next, right - left + 1)
        return head


def reverseNnode(head, n):
    if head is None or head.next is None:
        return head

    pre, cur, nex = None, head, head.next
    while n:
        cur.next = pre
        pre = cur
        cur = nex
        if nex:
            nex = nex.next
        n -= 1
    head.next = cur
    return pre
