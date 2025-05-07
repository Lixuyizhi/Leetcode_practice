# Definition for singly-linked list.
from fontTools.varLib.avarPlanner import normalizeDegrees


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.

    # 重载比较运算符，方便将 ListNode 加入最小堆
def __lt__(self, other):
    return self.val < other.val

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None

        dummy = ListNode(-1)
        p=dummy
        #优先级队列 最小堆
        pq=[]
        # 将 k 个链表的头结点加入最小堆
        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(pq, (head.val, i, head))
        while pq:
            val,i,node=heapq.heappop(pq)
            p.next =node
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
            p=p.next
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