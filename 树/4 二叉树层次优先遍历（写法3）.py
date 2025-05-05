# 创建树节点
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 定义state类用于记录树节点及路径权重和
class State(object):
    def __init__(self,root,weigh):
        self.root = root
        self.weigh = weigh

# 定义Solution类
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return
        q=deque()
        q.append(State(root,1))
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                print(f"当前的节点是:{cur.root.val},到达此节点的路径权重和是:{cur.weigh}")
                if cur.root.left is not None:
                    q.append(State(cur.root.left,cur.weigh+1))
                if cur.root.right is not None:
                    q.append(State(cur.root.right,cur.weigh+1))

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


