# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k) :
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None: return None
        # 区间 [a, b) 包含 k 个待反转元素
        a = b = head
        for _ in range(k):
            # 不足 k 个，不需要反转了
            if b is None: return head
            b = b.next
        # 反转前 k 个元素
        newHead = self.reverseN(a, k)
        # 此时 b 指向下一组待反转的头结点
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        return newHead

    # 上文实现的反转前 N 个节点的函数
    def reverseN(self, head, n):
        if head is None or head.next is None:
            return head
        pre, cur, nxt = None, head, head.next
        while n > 0:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt is not None:
                nxt = nxt.next
            n -= 1
        head.next = cur
        return pre

listnode=ListNode(1)
listnode.next=ListNode(2)
listnode.next.next=ListNode(3)
listnode.next.next.next=ListNode(4)
listnode.next.next.next.next=ListNode(5)
listnode.next.next.next.next.next=ListNode(6)
listnode.next.next.next.next.next.next=ListNode(7)

solution = Solution()
ans=solution.reverseKGroup(listnode, 2)
while ans is not None:
    print(ans.val)
    ans = ans.next
