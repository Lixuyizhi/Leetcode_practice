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
        while q:
            cur=q.popleft()
            print(cur.val,end=" ")
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)



# 创建一个二叉树
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(8)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# 创建Solution对象并调用levelOrder
solution = Solution()
result = solution.levelOrder(root)


