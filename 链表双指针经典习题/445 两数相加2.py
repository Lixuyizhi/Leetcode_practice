# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
         # 把链表元素转入栈中
        stk1 = []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        stk2 = []
        while l2:
            stk2.append(l2.val)
            l2 = l2.next

        # 接下来基本上是复用我在第 2 题的代码逻辑
        # 注意新节点要直接插入到 dummy 后面

        # 虚拟头结点（构建新链表时的常用技巧）
        dummy = ListNode(-1)

        # 记录进位
        carry = 0
        # 开始执行加法，两条链表走完且没有进位时才能结束循环
        while stk1 or stk2 or carry > 0:
            # 先加上上次的进位
            val = carry
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            # 处理进位情况
            carry = val // 10
            val = val % 10
            # 构建新节点，直接接在 dummy 后面
            newNode = ListNode(val)
            newNode.next = dummy.next
            dummy.next = newNode

        # 返回结果链表的头结点（去除虚拟头结点）
        return dummy.next