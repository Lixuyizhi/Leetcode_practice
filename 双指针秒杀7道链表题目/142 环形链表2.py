# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head
        p2 = head

        while p1 != None and p1.next != None:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                break
        if p1 == None or p1.next == None:
            return None
        p2 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p2.val


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=head.next.next

solution=Solution()
print(solution.detectCycle(head))