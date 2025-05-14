# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        # 后驱节点
        self.successor = None

    def reverseBetween(self, head, m, n):
        # base case
        if m == 1:
            return self.reverseN(head, n)
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    # 反转以 head 为起点的 n 个节点，返回新的头结点
    def reverseN(self, head, n):
        if n == 1:
            # 记录第 n + 1 个节点
            self.successor = head.next
            return head

        last = self.reverseN(head.next, n - 1)

        head.next.next = head
        head.next = self.successor
        return last