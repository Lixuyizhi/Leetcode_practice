# 创建树节点
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 定义Solution类
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return
        q=deque()
        q.append(root)
        level=1 #记录层数
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                print(f"当前的节点是:{cur.val},当前的层数是:{level}")
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            level+=1 #每一层结束后层数加1

# 创建一个二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# 创建Solution对象并调用levelOrder
solution = Solution()
solution.levelOrder(root)


