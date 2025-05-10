# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 从左向右移动的指针
    left = None
    # 从右向左移动的指针
    right = None

    # 记录链表是否为回文
    res = True

    def isPalindrome(self, head):
        self.left = head
        self.traverse(head)
        return self.res

    def traverse(self, right):
        if right is None:
            return

        # 利用递归，走到链表尾部
        self.traverse(right.next)

        # 后序遍历位置，此时的 right 指针指向链表右侧尾部
        # 所以可以和 left 指针比较，判断是否是回文链表
        if self.left.val != right.val:
            self.res = False
        self.left = self.left.next