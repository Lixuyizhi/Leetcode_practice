# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def isPalindrome(self, head):
        tem=[]
        while head:
            tem.append(head.val)
            head = head.next
        if tem == tem[::-1]:
            return True