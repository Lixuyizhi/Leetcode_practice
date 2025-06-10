# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        slow,fast=head,head
        while fast is not None:
            if slow.val!=fast.val:
                slow.next=fast
                slow=slow.next
            fast=fast.next
        slow.next=None
        return head

