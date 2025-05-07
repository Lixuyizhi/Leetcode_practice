# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = start + (end - start) // 2
        left = self.merge(lists, start, mid)
        right = self.merge(lists, mid + 1, end)

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        p = dummy

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1 is not None:
            p.next = l1
        if l2 is not None:
            p.next = l2

        return dummy.next

list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(4)

list2=ListNode(1)
list2.next=ListNode(5)
list2.next.next=ListNode(8)

list3=ListNode(1)
list3.next=ListNode(6)
list3.next.next=ListNode(7)

list=[list1,list2,list3]

solution = Solution()
ans=solution.mergeKLists(list)
while ans is not None:
    print(ans.val)
    ans = ans.next