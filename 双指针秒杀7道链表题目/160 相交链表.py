# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        # p1 指向 A 链表头结点，p2 指向 B 链表头结点
        p1, p2 = headA, headB
        while p1 != p2:
            # p1 走一步，如果走到 A 链表末尾，转到 B 链表
            p1 = p1.next if p1 else headB
            # p2 走一步，如果走到 B 链表末尾，转到 A 链表
            p2 = p2.next if p2 else headA
            if p1 ==None and p2== None:
                return None
        return p1

headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = ListNode(4)

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = headA.next.next

solution=Solution()# 调用方法，传入两个链表的头节点
intersection_node = solution.getIntersectionNode(headA, headB)

# 如果返回的 intersection_node 不为 None，表示有交点
if intersection_node:
    print(f"The intersection node's value is: {intersection_node.val}")
else:
    print("There is no intersection.")